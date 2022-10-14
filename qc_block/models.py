from django.db import models


# Create your models here.

class QC_Block_Model(models.Model):
    types_block = (
        ('OR7', 'OR7'),
        ('OR8', 'OR8'),
    )
    boolean = (
        ('OK', 'OK'),
        ('FALSE', 'FALSE'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField(auto_now=True)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    date_production = models.DateField()
    date_sampling = models.DateField()
    type_block = models.CharField(max_length=100, choices=types_block)
    thickness = models.IntegerField()
    length = models.DecimalField(decimal_places=1, max_digits=4)
    height = models.IntegerField(max_length=2)
    flatness = models.CharField(max_length=8, choices=boolean)
    mass = models.DecimalField(decimal_places=2, max_digits=4)
    surface_mass = models.DecimalField(decimal_places=2, max_digits=5)
    density = models.DecimalField(decimal_places=2, max_digits=6)
    water_absorption = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    ph = models.DecimalField(decimal_places=2, max_digits=4)
    bending_strength = models.DecimalField(decimal_places=2, max_digits=4)
    humidity = models.DecimalField(decimal_places=2, max_digits=4)
    non_conformity = models.CharField(max_length=1000, blank=True, null=True)
    action = models.CharField(max_length=1000, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
