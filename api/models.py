from django.db import models

class Cows(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    collar_id = models.CharField(max_length=10, unique=True)
    cow_number = models.CharField(max_length=30)
    collar_status = models.CharField(max_length=30)

    class Meta:
        db_table = 'cows'


