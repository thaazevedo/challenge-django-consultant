from django.db import models
from .campos_propostas import CamposProposta

# Modelo usado para elaboração
class FormProposta(models.Model):
  defaul = models.BooleanField(default=False, 
    help_text="Se selecionado este formulário será considerada padrão para visualização do proponente!")
  name   = models.CharField(verbose_name="Nome da proposta", max_length=255, unique=True)
  fields = models.ManyToManyField(CamposProposta, blank=True, 
    help_text="Selecione os campos para essa proposta!")
    

  def __str__(self):
    return self.name