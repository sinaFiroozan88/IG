from django.db import models


class Ultrax_Model(models.Model):
    targets = (
        ('k-', 'k-'),
        ('k-1', 'k-1'),
        ('k-2', 'k-2'),
    )
    Target_Product = models.CharField(choices=targets, max_length=6)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    published_date = models.DateField(auto_now=True)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=4)
    day = models.IntegerField(max_length=4)
    hour = models.IntegerField(max_length=2)
    line_qc = models.DecimalField(max_digits=4, decimal_places=2)
    office_qa = models.DecimalField(max_digits=4, decimal_places=2)
    kiln = models.DecimalField(max_digits=4, decimal_places=2)
    dif_line_kiln = models.DecimalField(max_digits=4, decimal_places=2)
    dif_qa_kiln = models.DecimalField(max_digits=4, decimal_places=2)
