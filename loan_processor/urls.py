from django.urls import path
from .views import send_proposta_processor

urlpatterns = [
  path("send_proposta/", send_proposta_processor, name="send_proposta")
]