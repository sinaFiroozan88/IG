from django.db import models


# Create your models here.

class Flexural_Bending_Strength_Model(models.Model):
    codes = (
        ('B', 'B'),
        ('B1', 'B1'),
    )
    published_date = models.DateField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True,
                               verbose_name='ثبت کننده')
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    code = models.CharField(max_length=3, choices=codes)
    f_flex = models.IntegerField(max_length=3)
    fm_flex = models.IntegerField(max_length=3)
    flexural_strength = models.DecimalField(decimal_places=2, max_digits=4)
    f_compress = models.IntegerField(max_length=3)
    fm_compress = models.IntegerField(max_length=3)
    compressive_strength = models.DecimalField(max_digits=4, decimal_places=2)
