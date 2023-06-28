from django.urls import path

from .views import home, get_form_proposta

urlpatterns = [
  path('', home, name="home"),
  path('create_proposta/', get_form_proposta, name="create_proposta"),
]