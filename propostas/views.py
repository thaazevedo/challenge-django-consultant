from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render, redirect

from propostas.models.form_propostas import FormProposta
from django.conf import settings

# Ao entrar na home do django, redireciona o user
## para a página de criar proposta
def home(request):
  return redirect('create_proposta')

# Pega o formulário da proposta para preenhimento dos
## campos necessários à proposta
def get_form_proposta(request):

  if FormProposta.objects.all().count() == 0:
    return HttpResponse({"Não existem formulários definidos!"})

  base_url = getattr(settings, "BASE_URL")

  tipo_campos = []
  proposta = None
  # Tratamento caso o ADMIN defina mais de um formulário com
  ## padrão, ele pega o último:
  try:
    try: 
      proposta = FormProposta.objects.get(default=True)
    except FormProposta.DoesNotExist:
      print("Não existe formulário padrão definido!")
      return HttpResponse({"Não existe formulário padrão definido!"})
  
  except FormProposta.MultipleObjectsReturned:
   
    proposta = FormProposta.objects.filter(default=True).last()

  if proposta:
    id_form = proposta.id
    for field in proposta.fields.all():
      if field.tipo not in tipo_campos:
        tipo_campos.append(field.tipo)

    tipo_campos.sort()

    context = {"proposta": proposta, "id_form": id_form,"field_types": tipo_campos, "base_url": base_url}

    return render(request, 'form_proposta.html', context, status=status.HTTP_200_OK)

