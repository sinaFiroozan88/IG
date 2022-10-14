from django.db import models


class QC_Block_Stucco_Model(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField(auto_now=True)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    hour = models.IntegerField(max_length=2)
    crystal_water_stucco = models.DecimalField(decimal_places=2, max_digits=4)
    einstrumenge = models.IntegerField(max_length=3)
    water_gypsum_ratio = models.DecimalField(max_digits=4, decimal_places=2)
    initial_setting_time = models.DecimalField(max_digits=4, decimal_places=1)
    final_setting_time = models.DecimalField(max_digits=4, decimal_places=1)
    retained_200 = models.DecimalField(decimal_places=2, max_digits=4)
    retained_500 = models.DecimalField(decimal_places=2, max_digits=4)
    non_conformity = models.CharField(max_length=1000, blank=True, null=True)
    action = models.CharField(max_length=1000, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
