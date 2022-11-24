from django.db import models

class Social(models.Model):
    facebook= models.URLField(max_length=255)
    email= models.URLField(max_length=255)
    twitter= models.URLField(max_length=255)
    linkedin= models.URLField(max_length=255)
    instagram= models.URLField(max_length=255)
    github= models.URLField(max_length=255)