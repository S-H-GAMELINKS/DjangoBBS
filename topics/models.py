from django.db import models

# Create your models here.
class Topic(models.Model):
    tittle_text = models.CharField(max_length=50)
    content_text = models.CharField(max_length=140)

class Comment(models.Model):
    content_text = models.CharField(max_length=140)