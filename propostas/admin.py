from django.contrib import admin
from django import forms

from propostas.models.options_campos import Option
from propostas.models.campos_propostas import CamposProposta
from propostas.models.form_propostas import FormProposta
from propostas.models.propostas import Proposta

admin.site.register(Option)

class CamposPropostaAdmin(admin.ModelAdmin):
  model = CamposProposta
  list_display = ('name', 'tipo')
  filter_horizontal = ('options',)

admin.site.register(CamposProposta, CamposPropostaAdmin)


class FormPropostaFormatDefault(forms.ModelForm):
  class Meta:
    model = FormProposta
    fields = '__all__'

  def clean_main(self):
    default = self.cleaned_data["default"]

    if default:
      forms = FormProposta.objects.all()
      for form in forms:
        form.default = False
        form.save()

    return self.cleaned_data["default"]

class FormPropostaAdmin(admin.ModelAdmin):
  form = FormPropostaFormatDefault
  list_display = ('name', 'default','campos')
  filter_horizontal = ('fields',)
  def campos(self, obj):
    return ', '.join([fields.name for fields in obj.fields.all()])
admin.site.register(FormProposta, FormPropostaAdmin)


class PropostaAdmin(admin.ModelAdmin):
  readonly_fields = ("needs_human_approval",)
  list_display = ('status', 'needs_human_approval', 'created_at')
  list_filter = ("status",)
admin.site.register(Proposta, PropostaAdmin)