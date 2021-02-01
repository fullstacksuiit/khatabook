
from django.db import models

# Create your models here.
class Party(models.Model):
    name = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    balance = models.FloatField(default=0.0)

    def __str__(self) :
        return self.name

class Transaction(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.FloatField(default=0.0)
    description = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.description