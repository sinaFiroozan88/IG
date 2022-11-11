from django.db import models

class Blane_Model(models.Model):
    number = models.IntegerField(max_length=5)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField()
    blane = models.IntegerField(max_length=6)
    initial_setting_time = models.DecimalField(max_digits=6, decimal_places=2)
    final_setting_time = models.DecimalField(max_digits=6, decimal_places=2)