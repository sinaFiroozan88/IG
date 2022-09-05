from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductModel(models.Model):
    causes = (
        ("اتمام ورودی", "اتمام ورودی"),
        ("خرابی مکانیکی", "خرابی مکانیکی"),
        ("خرابی الکتریکی", "خرابی الکتریکی")
    )
    stones = (
        ('Mix', 'Mix'),
        ('Mixe', 'Mixo'),
    )
    lines = (
        ('1', '1'),
        ('2', '2'),
    )
    line = models.CharField(choices=lines, max_length=20)
    published_date = models.DateField(auto_now=True)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)
    hour = models.IntegerField(max_length=2)
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, blank=True, null=True)
    main_product = models.CharField(max_length=200)
    quarry = models.CharField(choices=stones, max_length=200)
    kiln_feed_tonnage = models.IntegerField(validators=[
        MinValueValidator(5, 'enter a number from 5 to 25'),
        MaxValueValidator(25, 'enter a number from 5 to 25')
    ],)
    gas_valve_sp = models.IntegerField(validators=[
        MinValueValidator(0, 'enter a number from 0 to 10'),
        MaxValueValidator(10, 'enter a number from 0 to 10')
    ],)
    kiln_inlet_temp = models.IntegerField(validators=[
        MinValueValidator(400, 'enter a number from 400 to 900'),
        MaxValueValidator(900, 'enter a number from 400 to 900')
    ])
    setpoint_temp = models.IntegerField(validators=[
        MinValueValidator(100, 'enter a number form 100 to 150'),
        MaxValueValidator(150, 'enter a number form 100 to 150')
    ])
    kiln_outlet_temp = models.IntegerField(validators=[
        MinValueValidator(100, 'enter a number from 100 to 160'),
        MaxValueValidator(160, 'enter a number from 100 to 160')
    ])
    filter_fan_frequency = models.IntegerField(validators=[
        MinValueValidator(15, 'enter a number from 15 to 55'),
        MaxValueValidator(55, 'enter a number from 15 to 55')
    ])
    kiln_amper = models.IntegerField(validators=[
        MinValueValidator(30, 'enter a number from 30 to 65'),
        MaxValueValidator(65, 'enter a number from 30 to 65')
    ])
    kiln_negative_presure = models.IntegerField(validators=[
        MinValueValidator(0, 'enter a number from 0 to 0.7'),
        MaxValueValidator(0.7, 'enter a number from 0 to 0.7')
    ])
    stucco_temperature = models.IntegerField(validators=[
        MinValueValidator(0, 'enter a number from 0 to 160'),
        MaxValueValidator(160, 'enter a number from 0 to 160'),
    ])
    saparator_frequency = models.IntegerField(validators=[
        MinValueValidator(0, 'enter a number from 0 to 160'),
        MaxValueValidator(160, 'enter a number from 0 to 160')
    ])
    moleculator_N_frequency = models.IntegerField(validators=[
        MinValueValidator(20, 'enter a number from 20 to 50'),
        MaxValueValidator(50, 'enter a number from 20 to 50')
    ])
    moleculator_S_frequency = models.IntegerField(validators=[
        MinValueValidator(20, 'enter a number from 20 to 50'),
        MaxValueValidator(50, 'enter a number from 20 to 50')
    ])
    gas_counter_digit = models.IntegerField()
    energy_consumption = models.IntegerField()
    silo800_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    silo_knauf_1_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    silo_knauf_2_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    silo_block_1_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    silo_block_2_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    silo_emergency_1_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    silo_emergency_2_feed_time = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    work_without_output = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    stoppage = models.IntegerField(validators=[
        MinValueValidator(1, 'enter a number from 1 to 60'),
        MaxValueValidator(60, 'enter a number from 1 to 60')
    ])
    stoppage_cause = models.CharField(max_length=200, choices=causes)
    product_deviation_cause = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
