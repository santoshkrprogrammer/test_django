from django.db import models

# Create your models here.
class testmodel(models.Model):
    good=models.CharField(max_length=123)

class testmodelcheck(models.Model):
    good_check=models.CharField(max_length=123)
    great_check=models.CharField(max_length=123)