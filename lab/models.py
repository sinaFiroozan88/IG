from django.contrib import auth
from general.models import Hour, Quarry, Silo, Line, Action, Quarter
from django.db import models
from django.db.models import When
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator
import datetime as dt


class Lab(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author', blank=True, null=True,
                               verbose_name='ثبت کننده')

    line = models.ForeignKey('general.Line', on_delete=models.CASCADE,
                             verbose_name='خط')  # https://docs.djangoproject.com/en/3.0/ref
    mine = models.ForeignKey('general.Quarry', on_delete=models.CASCADE, verbose_name='معدن')
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE, verbose_name='ساعت آزمایش')
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, null=True)
    einstrumenge = models.PositiveSmallIntegerField(verbose_name='ملات',
                                                    validators=[
                                                        MinValueValidator(120, 'enter a number in range [120-160]'),
                                                        MaxValueValidator(160, 'enter a number in range [120-160]')],
                                                    )
    product_silo = models.ForeignKey('general.Silo', on_delete=models.CASCADE, verbose_name='محصول به سیلوی')
    free_moisture = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                        verbose_name='رطوبت آزاد')
    crystal_water_rawmat = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True,
                                               verbose_name='آب کریستال مواد خام',
                                               validators=[MinValueValidator(18.0, 'enter a number in range [18-20]'),
                                                           MaxValueValidator(20.0, 'enter a number in range [18-20]')],
                                               )
    purity_rm = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name='خلوص مواد خام')
    crystal_water_stucco = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='آب کریستال گچ',
                                               validators=[MinValueValidator(4.0, 'enter a number in range [4-7]'),
                                                           MaxValueValidator(7.0, 'enter a number in range [4-7]')],
                                               )
    water_gypsum_ratio = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='نسبت آب به گچ',
                                             validators=[MinValueValidator(0.5, 'enter a number in range [0.5-1]'),
                                                         MaxValueValidator(1.0, 'enter a number in range [0.5-1]')],
                                             help_text='this is an error message1'
                                             )
    initial_setting_time = models.DurationField(verbose_name='گیرش اولیه', help_text='[MM]:[ss] format')
    final_setting_time = models.DurationField(blank=True, verbose_name='گیرش ثانویه', validators=[])
    retained_63_micron = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                             verbose_name='الک 63 میکرون',
                                             validators=[MinValueValidator(20.0, 'enter a number in range [20-40]'),
                                                         MaxValueValidator(40.0, 'enter a number in range [20-40]')],
                                             )
    retained_200_micron = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                              verbose_name='الک 200 میکرون',
                                              validators=[MinValueValidator(2.0, 'enter a number in range [2-20]'),
                                                          MaxValueValidator(20.0, 'enter a number in range [2-20]')],
                                              )
    retained_500_micron = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                              verbose_name='الک 500 میکرون',
                                              validators=[MinValueValidator(0.0, 'enter a number in range [0-9]'),
                                                          MaxValueValidator(9.0, 'enter a number in range [0-9]')],
                                              )
    soluble_anhydrite = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                            verbose_name='انیدریت محلول')
    hemihydrate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True, verbose_name='همی هیدرات')
    low_solubility_anhydrite = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
                                                   verbose_name='انیدریت کم محلول')
    non_conformity = models.BooleanField(default=False, verbose_name='عدم انطباق')
    nonconf_P6 = models.BooleanField(default=False, verbose_name='عدم انطباق الک 63 میکرون',
                                     editable=When(non_conformity=True))
    nonconf_P5 = models.BooleanField(default=False, verbose_name='عدم انطباق الک 500 میکرون',
                                     editable=When(non_conformity=True))
    nonconf_P2 = models.BooleanField(default=False, verbose_name='عدم انطباق الک 200 میکرون',
                                     editable=When(non_conformity=True))
    nonconf_IS = models.BooleanField(default=False, verbose_name='عدم انطباق گیرش اولیه',
                                     editable=When(non_conformity=True))
    nonconf_FS = models.BooleanField(default=False, verbose_name='عدم انطباق گیرش ثانویه',
                                     editable=When(non_conformity=True))
    nonconf_EI = models.BooleanField(default=False, verbose_name='عدم انطباق وزن ملات',
                                     editable=When(non_conformity=True))
    nonconf_FM = models.BooleanField(default=False, verbose_name='عدم انطباق رطوبت آزاد',
                                     editable=When(non_conformity=True))
    nonconf_CS = models.BooleanField(default=False, verbose_name='عدم انطباق آب کریستال گچ',
                                     editable=When(non_conformity=True))
    # ACTION_CHOICES = {('CP', 'اجازه ارفاقی'), ('DP', 'اجازه انحراف'), ('SC', 'اسقاط'), ('RG', 'درجه بندی مجدد')}
    burner_sp_change = models.DecimalField(blank=True, null=True, verbose_name='تغییر دمای مشعل', max_digits=3,
                                           decimal_places=1, )
    call_to_operator = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='call_to_operator',
                                         null=True, blank=True, verbose_name='تماس با اپراتور')
    # action = models.CharField(max_length=5, choices=ACTION_CHOICES, blank=True, verbose_name='تعیین تکلیف')
    action = models.ForeignKey('general.Action', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='تعیین تکلیف')
    remarks = models.TextField(blank=True, verbose_name='توضیحات')
    created_date = models.DateField(default=dt.date.today, verbose_name='تاریخ ثبت داده')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
