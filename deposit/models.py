from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

def _generate_reference():
    get_random_string(length=8)


class Deposit(models.Model):
    amount = models.FloatField()
    note = models.CharField(max_length=1000)
    reference = models.CharField(max_length=255, default=_generate_reference)
    depositor = models.CharField(max_length=255)