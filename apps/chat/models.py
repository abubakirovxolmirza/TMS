from django.db import models
from apps.load.models import Load
from apps.auth.models import User

class Chat(models.Model):
    load_id = models.ForeignKey(Load, related_name='LoadChat', on_delete=models.CASCADE)
    message = models.CharField(max_length=300)
    user = models.ForeignKey(User, related_name='UserChat', on_delete=models.CASCADE)
