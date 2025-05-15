from django.db import models
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=100000)
    dt = models.DateTimeField(default=datetime.now(), blank=True)
