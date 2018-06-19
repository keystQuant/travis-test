from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField(blank=True, null=True)
