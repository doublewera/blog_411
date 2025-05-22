from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=1
    )
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=100000)
    dt = models.DateTimeField(default=datetime.now(), blank=True)
