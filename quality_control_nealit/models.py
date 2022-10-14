from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class QualityControlModel(models.Model):
    inlet = (
        ('خاک مواد خام', 'خاک مواد خام'),
        ('خاک مواد خام', 'خاک مواد خام')
    )
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField(auto_now=True,)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    hour = models.IntegerField(max_length=2)
    inlet_feed = models.CharField(choices=inlet, max_length=100)
    bag_number_2 = models.IntegerField(max_length=4)
    bag_number = models.DateField()
    free_moisture_filterdust = models.DecimalField(max_digits=4, decimal_places=2)
    crystal_water_filterdust = models.DecimalField(max_digits=4, decimal_places=2)
    purity_filterdust = models.DecimalField(max_digits=4, decimal_places=2)
    free_moisture_nealit = models.DecimalField(max_digits=4, decimal_places=2)
    retained_on_63 = models.DecimalField(max_digits=4, decimal_places=2)
    retained_on_200 = models.DecimalField(max_digits=4, decimal_places=2)
    retained_on_500 = models.DecimalField(max_digits=4, decimal_places=2)
    blaine_Nealit = models.IntegerField(validators=[
        MinValueValidator(6000, 'enter a number bigger than 6000')
    ])
    blaine_filterdust = models.IntegerField()
    blaine_after_mill = models.IntegerField()
    remarks = models.CharField(max_length=700)
