from django.db import models


class Ten_Sieve_Analysis_Model(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField(auto_now=True)
    year = models.IntegerField(max_length=5)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    sieve_40 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_63 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_90 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_100 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_200 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_300 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_400 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_500 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_600 = models.DecimalField(decimal_places=2, max_digits=4)
    sieve_1000 = models.DecimalField(decimal_places=2, max_digits=4)
