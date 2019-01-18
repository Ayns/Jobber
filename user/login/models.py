from django.db import models

# Create your models here.

class customer (models.Model):
    name = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=100, null=False)
    gst = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.name + " # " + self.city

