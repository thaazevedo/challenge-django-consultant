import requests

from celery import shared_task

@shared_task(bind=True)
def processor_proposta(self, document, name):
  print("SHARED TASK")
  processor_url  = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
  print(processor_url)
  data = {
    "document": document,
    "name": name
  }

  request  = requests.post(processor_url, data)

  response = request.text
  print(response)
  return response