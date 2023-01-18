from django.db import models


class Avg_Test_Production_Model(models.Model):
    lines = (
        ('1', '1'),
        ('2', '2'),
    )
    silos = (
        ('B', 'B'),
        ('K', 'K'),
    )
    published_date = models.DateField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    line = models.CharField(choices=lines, max_length=5)
    product_silo = models.CharField(choices=silos, max_length=5)
    usage = models.IntegerField(max_length=3)
    free_moisture = models.DecimalField(decimal_places=2, max_digits=4)
    crystal_water_raw_mat = models.DecimalField(decimal_places=2, max_digits=4)
    purity_of_raw_material = models.DecimalField(decimal_places=2, max_digits=4)
    crystal_water_of_stucco = models.DecimalField(decimal_places=2, max_digits=4)
    einstrumenge = models.DecimalField(decimal_places=1, max_digits=4)
    water_gypsum_ratio = models.DecimalField(decimal_places=2, max_digits=4)
    initial_setting_time = models.DecimalField(decimal_places=4, max_digits=7)
    final_setting_time = models.DecimalField(decimal_places=4, max_digits=7)
    retained_on_63 = models.DecimalField(decimal_places=2, max_digits=4)
    retained_on_200 = models.DecimalField(decimal_places=2, max_digits=4)
    retained_on_500 = models.DecimalField(decimal_places=2, max_digits=4)
    remarks = models.CharField(max_length=10000)
