from django.db import models

# MODELS
class Roll(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.name