from django.db import models

# Create your models here.
class Announcement(models.Model):
    title = models.CharField(max_length=300)
    passwd = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    club = models.CharField(max_length=100)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
