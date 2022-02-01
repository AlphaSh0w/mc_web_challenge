from django.db import models

# Create your models here.
class SuperHero(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    strength = models.IntegerField()
    speed = models.IntegerField()
    intelligence = models.IntegerField()

    def __str__(self):
        return self.name
    