from django.conf import settings
from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields.jsonb import JSONField


class DataStore(models.Model):
    key = models.CharField(max_length=255, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = JSONField(default=dict, blank=False)
