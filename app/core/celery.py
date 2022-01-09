import os
from celery import Celery
from app.core.config import settings
app = Celery("worker", broker=settings.CELERY_BROKER_URL)
