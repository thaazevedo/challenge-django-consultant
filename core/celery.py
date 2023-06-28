import os
from celery import Celery
from core.settings import CELERY_TIMEZONE

# Definindo configurações padrão do Django para o celery:
# Usado em manage.py:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# Definindo app
app = Celery('core')
# Config TIMEZONE
app.conf.enable_utc = False
app.conf.update(timezone=CELERY_TIMEZONE)
# Confis gerais
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()