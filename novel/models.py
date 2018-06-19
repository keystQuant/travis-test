from django.db import models


class Novel(models.Model):
    title = models.CharField(max_length=100)
    novel = models.TextField(blank=True, null=True)
