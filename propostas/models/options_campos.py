from django.db import models

# Modelo usado para campos de proposta que necessita de opções:
class Option(models.Model):
  option = models.CharField(max_length=255, 
    help_text="Escreva uma das opções que deverá ser mostrada ao proponente!")

  def __str__(self):
    return self.option

