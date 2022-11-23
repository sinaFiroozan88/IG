from django.db import models

# Create your models here.

class Block_Water_Acid_Model(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField()
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    ph = models.DecimalField(decimal_places=2, max_digits=4)