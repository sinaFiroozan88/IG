from django.db import models


class Silis_Model(models.Model):
    targets = (
        ('raw material kplus', 'raw material kplus'),
        ('aa', 'aa')
    )
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True,
                               verbose_name='ثبت کننده')
    published_date = models.DateField(auto_now=True)
    target_product = models.CharField(choices=targets, max_length=100)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    hour = models.IntegerField(max_length=2)
    free_moisture = models.DecimalField(max_digits=3, decimal_places=2)
    crystal_water_rawmat = models.DecimalField(decimal_places=2, max_digits=3)
    purity_rawmat = models.DecimalField(decimal_places=2, max_digits=5)
    sio2 = models.DecimalField(max_digits=5, decimal_places=2)
