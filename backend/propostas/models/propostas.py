from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver

from .form_propostas import FormProposta

class Proposta(models.Model):
  status_choice = [
    ('False', 'Negada'),
    ('True', 'Aprovada'),
    ('Human Approval', 'Avaliação necessária'),
  ]
  # Define o formulário correspondente
  form_proposta = models.ForeignKey(FormProposta, on_delete=models.CASCADE)
  status = models.CharField(max_length=255, choices=status_choice, blank=True, null=True)
  documentos = models.JSONField()
  # Caso aprovada pela API, deve ser aprovada por um humano
  needs_human_approval = models.BooleanField(default=False)
  # Para controle de atualização
  created_at  = models.DateTimeField(auto_now_add=True)
  updated_at  = models.DateTimeField(auto_now=True)

  def __str__(self):
    status = "Human Approval"
    if self.status == "True":
      status = "Aprovada"
    elif self.status == "False":
      status = "Negada"

    if self.needs_human_approval and self.status == "Human Approval":
      return "Avaliação humana necessária!"
    elif self.needs_human_approval and self.status != "Human Approval":
      return "Avaliação humana realizada: " + status
    else:
      return "Negada automaticamente"

  # def save(self, *args, **kwargs):
  #   if not self.needs_human_approval:
  #     self.status = "False"
  #   super(Proposta, self).save(*args, **kwargs)

@receiver(post_save, sender=Proposta)
def proposal_post_save(sender, instance, created, **kwargs):
    if not instance.needs_human_approval:
      instance.status = "False"
      instance.save()