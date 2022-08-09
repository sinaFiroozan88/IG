import datetime as dt
from django.utils import timezone
from django.db import models


class Food(models.Model):
    food = models.CharField(max_length=30)

    class Meta:
        ordering = ['food']

    def __str__(self):
        return self.food


class Ingredient(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='کاربر')
    date = models.DateTimeField(verbose_name='تاریخ')
    time = models.DateField(verbose_name='روز')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False)
    rice = models.IntegerField(verbose_name='برنج', null=True, blank=True)
    beef = models.IntegerField(verbose_name='گوشت گوساله', null=True, blank=True)
    lamb = models.IntegerField(verbose_name='گوشت گوسفند', null=True, blank=True)
    chicken_leg = models.IntegerField(verbose_name='ران مرغ', null=True, blank=True)
    chicken_breast = models.IntegerField(verbose_name='سینه مرغ', null=True, blank=True)
    fish = models.IntegerField(verbose_name='ماهی', null=True, blank=True)
    solid_oil = models.IntegerField(verbose_name='روغن جامد', null=True, blank=True)
    liquid_oil = models.IntegerField(verbose_name='روغن مایع', null=True, blank=True)
    beef_shank = models.IntegerField(verbose_name='قلم گوساله', null=True, blank=True)
    olive_oil = models.IntegerField(verbose_name='روغن زیتون', null=True, blank=True)
    macaroni = models.IntegerField(verbose_name='ماکارونی', null=True, blank=True)
    reshte_poloie = models.IntegerField(verbose_name='رشته پلویی', null=True, blank=True)
    rob_anar = models.IntegerField(verbose_name='رب انار', null=True, blank=True)
    egg = models.IntegerField(verbose_name='تخم مرغ', null=True, blank=True)
    animal_oil = models.IntegerField(verbose_name='روغن حیوانی', null=True, blank=True)
    butter_1 = models.IntegerField(verbose_name='کره', null=True, blank=True)
    lemon_juice_1 = models.IntegerField(verbose_name='آبلیمو یک نفره', null=True, blank=True)
    butter_bulk = models.IntegerField(verbose_name='کره فله ای', null=True, blank=True)
    tomato_paste = models.IntegerField(verbose_name='رب گوجه فرنگی', null=True, blank=True)
    lentil = models.IntegerField(verbose_name='عدس', null=True, blank=True)
    raisin = models.IntegerField(verbose_name='کشمش', null=True, blank=True)
    walnut = models.IntegerField(verbose_name='گردو', null=True, blank=True)
    split_peas = models.IntegerField(verbose_name='لپه', null=True, blank=True)
    red_beans = models.IntegerField(verbose_name='لوبیا قرمز', null=True, blank=True)
    tomato = models.IntegerField(verbose_name='گوجه فرنگی', null=True, blank=True)
    onion = models.IntegerField(verbose_name='پیاز', null=True, blank=True)
    potato = models.IntegerField(verbose_name='سیب زمینی', null=True, blank=True)
    broad_bean = models.IntegerField(verbose_name='باقالی', null=True, blank=True)
    celery = models.IntegerField(verbose_name='کرفس', null=True, blank=True)
    green_bean = models.IntegerField(verbose_name='لوبیا سبز', null=True, blank=True)
    eggplant = models.IntegerField(verbose_name='بادمجان', null=True, blank=True)
    amani_lemon = models.IntegerField(verbose_name='لیمو امانی', null=True, blank=True)
    lemon = models.IntegerField(verbose_name='لیمو', null=True, blank=True)
    sabzi_kuku = models.IntegerField(verbose_name='سبزی کوکو', null=True, blank=True)
    sabzi_qorme = models.IntegerField(verbose_name='سبزی قورمه', null=True, blank=True)
    sabzi_poloie = models.IntegerField(verbose_name='سبزی پلویی', null=True, blank=True)
    garlic = models.IntegerField(verbose_name='سیر', null=True, blank=True)
    bell_pepper = models.IntegerField(verbose_name='فلفل دلمه', null=True, blank=True)
    mushroom = models.IntegerField(verbose_name='قارچ', null=True, blank=True)
    peas = models.IntegerField(verbose_name='نخود فرنگی', null=True, blank=True)
    coriander = models.IntegerField(verbose_name='گشنیز', null=True, blank=True)
    dry_savory = models.IntegerField(verbose_name='مرزه خشک', null=True, blank=True)
    dried_tarragon = models.IntegerField(verbose_name='ترخون خشک', null=True, blank=True)
    spearmint = models.IntegerField(verbose_name='نعناع', null=True, blank=True)
    jafari = models.IntegerField(verbose_name='جعفری', null=True, blank=True)
    reyhan = models.IntegerField(verbose_name='ریحان', null=True, blank=True)
    pickle = models.IntegerField(verbose_name='خیارشور', null=True, blank=True)
    carrot = models.IntegerField(verbose_name='هویج', null=True, blank=True)
    shevid = models.IntegerField(verbose_name='شوید', null=True, blank=True)
    saffron = models.IntegerField(verbose_name='زعفران', null=True, blank=True)
    verjuice = models.IntegerField(verbose_name='آبغوره', null=True, blank=True)
    lemon_juice = models.IntegerField(verbose_name='آبلیمو', null=True, blank=True)
    white_vinegar = models.IntegerField(verbose_name='سرکه سقید', null=True, blank=True)
    white_flour = models.IntegerField(verbose_name='آرد سفید', null=True, blank=True)
    toasted_flour = models.IntegerField(verbose_name='آرد سوخاری', null=True, blank=True)
    toasted_powder = models.IntegerField(verbose_name='پودر سوخاری', null=True, blank=True)
    rice_flour = models.IntegerField(verbose_name='آرد برنج', null=True, blank=True)
    chickpea_flour = models.IntegerField(verbose_name='آرد نخود', null=True, blank=True)
    sugar = models.IntegerField(verbose_name='شکر', null=True, blank=True)
    yogurt = models.IntegerField(verbose_name='ماست', null=True, blank=True)
    sumac = models.IntegerField(verbose_name='سماق', null=True, blank=True)
    starch = models.IntegerField(verbose_name='نشاسته', null=True, blank=True)
    vinegar = models.IntegerField(verbose_name='سرکه', null=True, blank=True)
    mustard = models.IntegerField(verbose_name='سس خردل', null=True, blank=True)
    sauce = models.IntegerField(verbose_name='سس', null=True, blank=True)
    rosewater = models.IntegerField(verbose_name='گلاب', null=True, blank=True)
    barberry = models.IntegerField(verbose_name='زرشک', null=True, blank=True)
    rock_salt = models.IntegerField(verbose_name='سنگ نمک', null=True, blank=True)
    pepper = models.IntegerField(verbose_name='فلفل', null=True, blank=True)
    milk = models.IntegerField(verbose_name='شیر', null=True, blank=True)
    salt = models.IntegerField(verbose_name='نمک', null=True, blank=True)

    class Meta:
        ordering = ['food']

    def __str__(self):
        return self.food


class DailyMeal(Ingredient):
    quantity = models.IntegerField(verbose_name='تعداد غذا')

    class Meta:
        ordering = ['food']

    def __str__(self):
        return str(self.food)
