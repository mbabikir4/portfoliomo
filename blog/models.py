from django.db import models

# Create your models here.
class Blag(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    time = models.DateField()

    def __str__(self):
        return self.title