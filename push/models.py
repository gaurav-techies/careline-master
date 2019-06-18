from django.db import models
from .tasks import send_push


class PushNotify(models.Model):
    """
    Push Notification App
    """
    msg = models.CharField(max_length=110)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_push.delay(self.msg)

    def __str__(self):
        return self.msg