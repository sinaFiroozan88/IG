from django.db import models


# Create your models here.

class QC_Retest_Model(models.Model):
    lines = (
        ('1', '1'),
        ('2', '2')
    )
    mines = (
        ('mix', 'mix'),
        ('cheshme', 'cheshme'),
        ('gorgine', 'gorgine'),
        ('saran', 'saran')
    )
    products = (
        ('kenaf', 'kenaf'),
        ('no product', 'no product'),
        ('block', 'block')
    )
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField(auto_now=True, )
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    hour = models.IntegerField(max_length=2)
    line = models.CharField(max_length=10, choices=lines)
    product_silo = models.CharField(max_length=40, choices=products)
    mine = models.CharField(max_length=40, choices=mines)
    free_moisture = models.DecimalField(decimal_places=2, max_digits=5)
    crystal_water_raw_mat = models.DecimalField(decimal_places=2, max_digits=5)
    Purity_raw_mat = models.DecimalField(decimal_places=10, max_digits=100)
    crystal_water_stucco = models.DecimalField(decimal_places=2, max_digits=5)
    Einstrumenge = models.IntegerField()
    Water_gypsum_ratio = models.DecimalField(decimal_places=2, max_digits=5)
    initial_setting_time = models.DecimalField(decimal_places=4, max_digits=7)
    final_setting_time = models.DecimalField(decimal_places=4, max_digits=7)
    retained_on_63 = models.DecimalField(decimal_places=1, max_digits=5)
    retained_on_200 = models.DecimalField(decimal_places=1, max_digits=5)
    retained_on_500 = models.DecimalField(decimal_places=1, max_digits=5)
    non_conformity = models.CharField(max_length=1000)
    actions = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000)
