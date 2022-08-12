import datetime

from django.db import models
import datetime as dt


class Hour(models.Model):
    HOUR_CHOICES = [(dt.time(hour=x), '{:02d}:00'.format(x)) for x in range(0, 24)]
    index = models.IntegerField(verbose_name='ردیف')
    hour = models.TimeField(verbose_name='ساعت آزمایش', choices=HOUR_CHOICES)
    active = models.BooleanField(verbose_name='فعال', default=True)

    # def __str__(self):
    #     hour = self.hour
    #     return hour.strftime('%H')
    # return hour.strftime('%H')


class Quarter(models.Model):
    hour = models.ForeignKey(Hour, models.CASCADE, verbose_name='ربع ساعت')
    quarter = models.TimeField()

    def __str__(self):
        return self.quarter.strftime('%H:%M')


class Quarry(models.Model):
    index = models.IntegerField(verbose_name='ردیف')
    quarry = models.CharField(max_length=30, verbose_name='quarry')
    quarry_p = models.CharField(max_length=30, verbose_name='معادن')
    active = models.BooleanField(verbose_name='فعال', default=True)

    def __str__(self):
        return self.quarry


class Line(models.Model):
    index = models.IntegerField(verbose_name='ردیف')
    line = models.CharField(max_length=10, verbose_name='line')
    line_p = models.CharField(max_length=10, verbose_name='خط تولید')
    active = models.BooleanField(verbose_name='فعال', default=True)

    def __str__(self):
        return self.line


class Silo(models.Model):
    index = models.IntegerField(verbose_name='ردیف')
    silo = models.CharField(max_length=30, verbose_name='silo')
    silo_p = models.CharField(max_length=30, verbose_name='سیلو')
    active = models.BooleanField(verbose_name='فعال', default=True)

    def __str__(self):
        return self.silo


class Action(models.Model):
    index = models.IntegerField(verbose_name='ردیف')
    action = models.CharField(max_length=30, verbose_name='سیلو')
    action_p = models.CharField(max_length=30, verbose_name='سیلو')
    active = models.BooleanField(verbose_name='فعال', default=True)

    def __str__(self):
        return self.action_p
