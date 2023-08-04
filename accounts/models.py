from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=100)
    access = models.BooleanField(default=False)

    def __str__(self):
        return self.email
