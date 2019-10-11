from django.db import models
from s3direct.fields import S3DirectField


class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    year_of_manufacture = models.CharField(max_length=255, blank=False, null=False)
    price = models.CharField(max_length=255, blank=False, null=False)
    image = S3DirectField(dest='primary_destination', blank=True)
    video = S3DirectField(dest='primary_destination', blank=True)

    def __str__(self):
        """
        Return a string representation of the model instance
        """
        return f"{self.name} ({self.year_of_manufacture}) - {self.price}"
