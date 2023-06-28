import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from propostas.models.propostas import Proposta
from propostas.models.form_propostas import FormProposta

from propostas.tasks import processor_proposta

# Parte responsável pela anaviação da proposta
## na API de avaliação automática:
@api_view(['POST'])
def send_proposta_processor(request):

  # Recebendo informações do formulários
  document = request.data['document']
  name = request.data['name']
  id = request.data['id']
  
  # Fetch API
  result = processor_proposta(document, name)
  json_result = json.loads(result)

  # De acordo com o retorno da API, preencha os dados
  state='False'
  if json_result["approved"]:
    state='Human Approval'

  # Considerando as informações, pegue o formulário correspondente
  ## à proposta e crie a mesma
  form = FormProposta.objects.get(id=id)
  Proposta.objects.create(
    form_proposta=form,
    documentos=document,
    status=state,
    needs_human_approval=json_result["approved"]
  )

  context = {"status": state}
  return Response(context)