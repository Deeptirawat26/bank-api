from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=500)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        db_table = 'banks'
        managed = False

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, unique=True,primary_key=True)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=5000)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

    class Meta:
        db_table = 'branches'
        managed = False