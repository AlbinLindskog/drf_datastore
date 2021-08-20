from django.conf import settings
from django.db import models

try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields.jsonb import JSONField


class DataStore(models.Model):
    key = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data = JSONField(default=dict, blank=False)

    class Meta:
        unique_together = ('key', 'user')
        indexes = [
            models.Index(fields=['key', 'user']),
        ]
