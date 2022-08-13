from django.db import models


class Block(models.Model):
    days = (
        ('شنبه', 'شنبه'),
        ('یکشنبه', 'یکشنبه'),
        ('دوشنبه', 'دوشنبه'),
        ('سه شنبه', 'سه شنبه'),
        ('چهارشنبه', 'چهارشنبه'),
        ('پنجشنبه', 'پنجشنبه'),
        ('جمعه', 'جمعه')
    )
    day = models.CharField(verbose_name='روز', max_length=8, choices=days)
    date = models.DateField(verbose_name='تاریخ', )
    # consumption
    block_stucco = models.IntegerField(verbose_name='مصرف گچ (تن)')
    water_consumption = models.IntegerField(verbose_name='مصرف آب (لیتر)')
    gas_consumption = models.IntegerField(verbose_name='مصرف گاز (متر مکعب)')
    elec_consumption = models.IntegerField(verbose_name='مصرف برق (کیلو وات)')
    gasoil_consumption = models.IntegerField(verbose_name='مصرف گازوئیل (لیتر)')
    # production
    block7_prod = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_prod = models.IntegerField(verbose_name='بلوک 8 سانت')
    block8mr_prod = models.IntegerField(verbose_name='بلوک 8 عایق')
    total_block_prod = models.IntegerField(verbose_name='جمع کل', blank=True, null=True)
    # packing
    block7_packing = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_packing = models.IntegerField(verbose_name='بلوک 8 سانت')
    block8mr_packing = models.IntegerField(verbose_name='بلوک 8 عایق')
    total_block_packing = models.IntegerField(verbose_name='جمع کل', blank=True, null=True)
    # packing waste
    block7_waste = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_waste = models.IntegerField(verbose_name='بلوک 8 سانت')
    block8mr_waste = models.IntegerField(verbose_name='بلوک 8 عایق')
    total_block_waste = models.IntegerField(verbose_name='جمع کل', blank=True, null=True)
    # block machinery
    block7_operation = models.IntegerField(verbose_name='بلوک 7 سانت')
    block8_operation = models.IntegerField(verbose_name='بلوک 8 سانت')
    dryer_operation = models.IntegerField(verbose_name='خشک کن')
    total_block_operation = models.IntegerField(verbose_name='جمع کل', blank=True, null=True)
    # block inventory
    block7_packing_inventory = models.IntegerField(verbose_name='بسته بندی بلوک 7')
    block7_dryer_inventory = models.IntegerField(verbose_name="خشک کن بلوک 7")
    block7_rack_inventory = models.IntegerField(verbose_name="خشک باز بلوک 7")

    block8_packing_inventory = models.IntegerField(verbose_name='بسته بندی بلوک 8')
    block8_dryer_inventory = models.IntegerField(verbose_name="خشک کن بلوک 8")
    block8_rack_inventory = models.IntegerField(verbose_name="خشک باز بلوک 8")

    block8mr_packing_inventory = models.IntegerField(verbose_name='بسته بندی بلوک 8 عایق')
    block8mr_dryer_inventory = models.IntegerField(verbose_name="خشک کن بلوک 8 عایق")
    block8mr_rack_inventory = models.IntegerField(verbose_name="خشک باز بلوک 8 عایق")

    betogips_inventory = models.IntegerField(verbose_name='دسته بندی بتو گیپس', blank=True, null=True)
    betogips_wased = models.IntegerField(verbose_name='خشک کن بتو گیپس', blank=True, null=True)

    # block stoppage
    block7_rawmat_stoppage = models.IntegerField(verbose_name='مواد اولیه')
    block7_operator_stoppage = models.IntegerField(verbose_name='نیروی انسانی')
    block7_mechanical16_stoppage = models.IntegerField(verbose_name='+16 مکانیکال')
    block7_electrical16_stoppage = models.IntegerField(verbose_name='+الکتریکال 16')
    block7_mechanical_stoppage = models.IntegerField(verbose_name='-16 مکانیکال')
    block7_electrical_stoppage = models.IntegerField(verbose_name='-16 الکتریکال')
    block7_noNeeded_stoppage = models.IntegerField(verbose_name='عدم نیاز')
    block7_rackFull_stoppage = models.IntegerField(verbose_name='کمبود فضای تولید')
    block7_gasoil_stoppage = models.IntegerField(verbose_name='گازوئیل')
    block7_gas_stoppage = models.IntegerField(verbose_name='گاز')
    block7_elec_stoppage = models.IntegerField(verbose_name='برق')
    block7_total_stoppage = models.IntegerField(verbose_name='جمع توقفات', blank=True, null=True)

    block8_rawmat_stoppage = models.IntegerField(verbose_name='مواد اولیه')
    block8_operator_stoppage = models.IntegerField(verbose_name='نیروی انسانی')
    block8_mechanical16_stoppage = models.IntegerField(verbose_name='+16 مکانیکال')
    block8_electrical16_stoppage = models.IntegerField(verbose_name='+الکتریکال 16')
    block8_mechanical_stoppage = models.IntegerField(verbose_name='-16 مکانیکال')
    block8_electrical_stoppage = models.IntegerField(verbose_name='-16 الکتریکال')
    block8_noNeeded_stoppage = models.IntegerField(verbose_name='عدم نیاز')
    block8_rackFull_stoppage = models.IntegerField(verbose_name='کمبود فضای تولید')
    block8_gasoil_stoppage = models.IntegerField(verbose_name='گازوئیل')
    block8_gas_stoppage = models.IntegerField(verbose_name='گاز')
    block8_elec_stoppage = models.IntegerField(verbose_name='برق')
    block8_total_stoppage = models.IntegerField(verbose_name='جمع توقفات', blank=True, null=True)

    dryer_rawmat_stoppage = models.IntegerField(verbose_name='مواد اولیه')
    dryer_operator_stoppage = models.IntegerField(verbose_name='نیروی انسانی')
    dryer_mechanical16_stoppage = models.IntegerField(verbose_name='+16 مکانیکال')
    dryer_electrical16_stoppage = models.IntegerField(verbose_name='+الکتریکال 16')
    dryer_mechanical_stoppage = models.IntegerField(verbose_name='-16 مکانیکال')
    dryer_electrical_stoppage = models.IntegerField(verbose_name='-16 الکتریکال')
    dryer_noNeeded_stoppage = models.IntegerField(verbose_name='عدم نیاز')
    dryer_rackFull_stoppage = models.IntegerField(verbose_name='کمبود فضای تولید')
    dryer_gasoil_stoppage = models.IntegerField(verbose_name='گازوئیل')
    dryer_gas_stoppage = models.IntegerField(verbose_name='گاز')
    dryer_elec_stoppage = models.IntegerField(verbose_name='برق')
    dryer_total_stoppage = models.IntegerField(verbose_name='جمع توقفات', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_block_prod = self.block7_prod + self.block8_prod + self.block8mr_prod
        self.total_block_packing = self.block7_packing + self.block8_packing + self.block8mr_packing
        self.total_block_operation = self.block7_operation + self.block8_operation + self.dryer_operation
        self.total_block_waste = self.block7_waste + self.block8_waste + self.block8mr_waste
        self.dryer_total_stoppage = self.dryer_rawmat_stoppage + self.dryer_operator_stoppage + self.dryer_mechanical16_stoppage + self.dryer_electrical16_stoppage + self.dryer_mechanical_stoppage + self.dryer_electrical_stoppage + self.dryer_noNeeded_stoppage + self.dryer_rackFull_stoppage + self.dryer_gasoil_stoppage + self.dryer_gas_stoppage + self.dryer_elec_stoppage
        self.block7_total_stoppage = self.block7_rawmat_stoppage + self.block7_operator_stoppage + self.block7_mechanical16_stoppage + self.block7_electrical16_stoppage + self.block7_mechanical_stoppage + self.block7_electrical_stoppage + self.block7_noNeeded_stoppage + self.block7_rackFull_stoppage + self.block7_gasoil_stoppage + self.block7_gas_stoppage + self.block7_elec_stoppage
        self.block8_total_stoppage = self.block8_rawmat_stoppage + self.block8_operator_stoppage + self.block8_mechanical16_stoppage + self.block8_electrical16_stoppage + self.block8_mechanical_stoppage + self.block8_electrical_stoppage + self.block8_noNeeded_stoppage + self.block8_rackFull_stoppage + self.block8_gasoil_stoppage + self.block8_gas_stoppage + self.block8_elec_stoppage
        super(Block, self).save()
