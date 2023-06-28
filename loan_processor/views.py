import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from propostas.models.propostas import Proposta
from propostas.models.form_propostas import FormProposta

from propostas.tasks import processor_proposta

@api_view(['POST'])
def send_proposta_processor(request):
  print(request.data)
  document = request.data['document']
  name = request.data['name']
  id = request.data['id']
  
  result = processor_proposta(document, name)
  print(result)
  json_result = json.loads(result)

  state='False'
  needs_human_approval = False
  if json_result["approved"]:
    state='Human Approval'
    needs_human_approval=True
  # else:
    # state = "False"
    # needs_human_approval=False
  print(state)
  form = FormProposta.objects.get(id=id)
  print(form)
  Proposta.objects.create(
    form_proposta=form,
    documentos=document,
    status=state,
    needs_human_approval=json_result["approved"]
  )
  print(state)
  context = {"status": state}
  print(context)
  # return Response(request, context)
  return Response(context)