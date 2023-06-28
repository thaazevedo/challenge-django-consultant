from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render, redirect

from propostas.models.form_propostas import FormProposta
from django.conf import settings

def home(request):
  return redirect('create_proposta')


def get_form_proposta(request):

  if FormProposta.objects.all().count() == 0:
    return HttpResponse({"Não existem formulários definidos!"})

  base_url = getattr(settings, "BASE_URL")
  print(base_url)
  tipo_campos = []
  proposta = None
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

