from django.utils import timezone

from django.db import models
from general.models import Hour, Line
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator, DecimalValidator
import datetime


class Nealit(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='nealit_author', blank=True, null=True, verbose_name='ثبت کننده')
    date = models.DateField(verbose_name='تاریخ تولید نئالیت', default = timezone.now)
    jumbo_no = models.PositiveIntegerField(verbose_name='شماره کیسه', unique=True)
    jumbo_no_month = models.CharField(max_length=50, verbose_name='شماره ماه کیسه')
    feed_material = models.CharField(max_length=50, verbose_name='بار ورودی',
                                     choices=[('مواد خام', 'مواد خام'), ('کراشر', 'کراشر'), ('میکس', 'میکس'), ('کناف گچ', 'کناف گچ')])
    input_temp = models.SmallIntegerField(verbose_name='دمای ورودی' )
    output_temp = models.SmallIntegerField(verbose_name='دمای خروجی')
    line = models.ForeignKey('general.Line', on_delete=models.CASCADE, verbose_name='خط')
    jumbo_time0 = models.DateTimeField(blank=True, null=True,verbose_name='زمان شروع جامبو')
    jumbo_time1 = models.DateTimeField(blank=True, null=True, verbose_name='زمان پایان جامبو')
    jumbo_filled_time = models.DurationField(verbose_name='زمان پر شدن کیسه')
    jumbo_weight = models.PositiveSmallIntegerField(max_length=4, validators=[MaxLengthValidator(1500, 'عددی کمتر از 1500 قرار دهید')])
    ton_per_hour = models.PositiveSmallIntegerField(verbose_name='تناژ ساعتی')
    ton_per_minute = models.PositiveSmallIntegerField(verbose_name='تناژ دقیقه ای')
    additive_type = models.CharField(max_length=50, verbose_name='نوع افزودنی')
    remark = models.TextField(blank=True, verbose_name='توضیحات')


class Suger(models.Model):
    suger_time0 = models.DateTimeField(verbose_name='زمان ریختن شکر')
    suger_time1 = models.DateTimeField(verbose_name='زمان اتمام شکر')
    suger_filled_time = models.DurationField(verbose_name='زمان پر شدن',blank=True, null=True)
    suger_weight = models.IntegerField(verbose_name='وزن کیسه شکر', choices=[(50,50), (60,60), (25,25), (30,30)], default=50)
    suger_per_minute = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    suger_per_hour = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    remark = models.TextField(blank=True, verbose_name='توضیحات')

    def fill_calc(self):
        self.suger_filled_time = self.suger_time1 - self.suger_time0

        self.save()











