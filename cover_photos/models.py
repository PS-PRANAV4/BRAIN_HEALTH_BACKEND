
from pyexpat import model
from django.db import models

# Create your models here.


class CoverPhtos(models.Model):
    cover_image = models.ImageField(upload_to = 'photos/cover',blank = True, null = True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Icons(models.Model):
    icons = models.ImageField(upload_to = 'photos/icon', blank = True, null = True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name