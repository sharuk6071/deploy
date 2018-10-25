from django.db import models

# Create your models here.
class ido(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(('password'), max_length=128)

    def __str__(self):
        return self.username
