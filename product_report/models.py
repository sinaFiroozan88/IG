from django.db import models


class ProductReport(models.Model):
    day = (
        ("شنبه", 'شنبه'),
        ("یک شنبه", 'یک شنبه'),
        ("دو شنبه", 'دو شنبه'),
        ("سه شنبه", 'سه شنبه'),
        ("چهار شنبه", 'چهار شنبه'),
        ("پنج شنبه", 'پنج شنبه'),
        ("جمعه", 'جمعه')
    )
    date = models.DateField(verbose_name='تاریخ', )
    # crasher operation
    Machinery = models.IntegerField()
    Crasher_Elec_Consumption = models.IntegerField()
    Rockstone_Shortage = models.IntegerField()
    No_Needed = models.IntegerField()
    Electrical_Fault = models.IntegerField()
    Mechanical_Fault = models.IntegerField()
    Operator_Fault = models.IntegerField()
    Total_Fault = models.IntegerField(blank=True, null=True)
    # Raw Material Consumption
    Kenaf_Rawmat_Consumption_1 = models.IntegerField()
    Kenaf_Rawmat_Consumption_2 = models.IntegerField()
    Kenaf_Stucco_Prod_1 = models.IntegerField()
    Kenaf_Stucco_Prod_2 = models.IntegerField()
    Ordinary_RawMat_Consumption_1 = models.IntegerField()
    Ordinary_RawMat_Consumption_2 = models.IntegerField()
    Ordinary_Stucco_Prod_1 = models.IntegerField()
    Ordinary_Stucco_Prod_2 = models.IntegerField()
    Block_RawMat_Consumption_1 = models.IntegerField()
    Block_RawMat_Consumption_2 = models.IntegerField()
    Block_Stucco_Prod_1 = models.IntegerField()
    Block_Stucco_Prod_2 = models.IntegerField()
    Nealit_RawMat_Consumption = models.IntegerField()
    Nealit_Sugar_Consumption = models.IntegerField()
    Nealit_Prod = models.IntegerField()
    Total_Consumption_1 = models.IntegerField(blank=True, null=True)
    Total_Consumption_2 = models.IntegerField(blank=True, null=True)
    Total_Prod_1 = models.IntegerField(blank=True, null=True)
    Total_Prod_2 = models.IntegerField(blank=True, null=True)
    # stoppage causes
    No_Needed_1 = models.IntegerField()
    No_Needed_Nealit = models.IntegerField()
    No_Needed_2 = models.IntegerField()
    Electrical_Stoppage_1 = models.IntegerField()
    Electrical_Stoppage_2 = models.IntegerField()
    Blackout_Stoppage_1 = models.IntegerField()
    Blackout_Stoppage_2 = models.IntegerField()
    Blackout_Stoppage_Nealit = models.IntegerField()
    Electrical_Stoppage_Nealit = models.IntegerField()
    Mechanical_Stoppage_1 = models.IntegerField()
    Mechanical_Stoppage_2 = models.IntegerField()
    Mechanical_Stoppage_Nealit = models.IntegerField()
    Gas_Cutout_Stoppage_1 = models.IntegerField()
    Gas_Cutout_Stoppage_2 = models.IntegerField()
    Gas_Cutout_Stoppage_Nealit = models.IntegerField()
    Gasoil_Cutout_Stoppage_1 = models.IntegerField()
    Gasoil_Cutout_Stoppage_2 = models.IntegerField()
    Gasoil_Cutout_Stoppage_Nealit = models.IntegerField()
    Initial_Start_Stoppage_1 = models.IntegerField()
    Initial_Start_Stoppage_2 = models.IntegerField()
    Initial_Start_Stoppage_Nealit = models.IntegerField()
    End_production_Stoppage_1 = models.IntegerField()
    End_production_Stoppage_2 = models.IntegerField()
    End_production_Stoppage_Nealit = models.IntegerField()
    Operator_Base_Stoppage_1 = models.IntegerField()
    Operator_Base_Stoppage_2 = models.IntegerField()
    Operator_Base_Stoppage_Nealit = models.IntegerField()
    Total_Stoppage_1 = models.IntegerField(blank=True, null=True)
    Total_Stoppage_2 = models.IntegerField(blank=True, null=True)
    Total_Stoppage_Nealit = models.IntegerField(blank=True, null=True)
    # silo inventories
    Silo_1_Inventory = models.IntegerField()
    Silo_2_Inventory = models.IntegerField()
    Block_Silo_N_Inventory = models.IntegerField()
    Block_Silo_S_Inventory = models.IntegerField()
    Silo_800_Inventory = models.IntegerField()
    # energy consumption
    Gas_Consumption_AM_1 = models.IntegerField()
    Gas_Consumption_PM_1 = models.IntegerField()
    Gas_Consumption_AM_2 = models.IntegerField()
    Gas_Consumption_PM_2 = models.IntegerField()
    Gasoil_Consumption_AM_1 = models.IntegerField()
    Gasoil_Consumption_PM_1 = models.IntegerField()
    Gasoil_Consumption_AM_2 = models.IntegerField()
    Gasoil_Consumption_PM_2 = models.IntegerField()
    Gas_Temperature_1 = models.IntegerField()
    Gas_Temperature_2 = models.IntegerField()
    Gas_Presure_1 = models.IntegerField()
    Gas_Presure_2 = models.IntegerField()

    def save(self, *args, **kwargs):
        self.Total_Fault = self.Machinery + self.Operator_Fault + self.Mechanical_Fault + self.Electrical_Fault + self.No_Needed
        self.Total_Consumption = self.Block_RawMat_Consumption_1 + self.Block_RawMat_Consumption_2 + self.Nealit_RawMat_Consumption + self.Kenaf_Rawmat_Consumption_1 + self.Kenaf_Rawmat_Consumption_2 + self.Ordinary_RawMat_Consumption_1 + self.Ordinary_RawMat_Consumption_2
        self.Total_Prod_1 = self.Kenaf_Stucco_Prod_1 + self.Ordinary_Stucco_Prod_1 + self.Block_Stucco_Prod_1
        self.Total_Prod_2 = self.Kenaf_Stucco_Prod_2 + self.Ordinary_Stucco_Prod_2 + self
        self.Total_Stoppage_1 = self.Blackout_Stoppage_1 + self.Electrical_Stoppage_1 + self.End_production_Stoppage_1 + self.No_Needed_1 + self.Mechanical_Stoppage_1 + self.Gas_Cutout_Stoppage_1 + self.Gasoil_Cutout_Stoppage_1 + self.Initial_Start_Stoppage_1 + self.Operator_Base_Stoppage_1
        self.Total_Stoppage_2 = self.Blackout_Stoppage_2 + self.Electrical_Stoppage_2 + self.End_production_Stoppage_2 + self.No_Needed_2 + self.Mechanical_Stoppage_2 + self.Gas_Cutout_Stoppage_2 + self.Gasoil_Cutout_Stoppage_2 + self.Initial_Start_Stoppage_2 + self.Operator_Base_Stoppage_2
        self.Total_Stoppage_Nealit = self.Blackout_Stoppage_Nealit + self.Electrical_Stoppage_Nealit + self.End_production_Stoppage_Nealit + self.No_Needed_Nealit + self.Mechanical_Stoppage_Nealit + self.Gas_Cutout_Stoppage_Nealit + self.Gasoil_Cutout_Stoppage_Nealit + self.Initial_Start_Stoppage_Nealit + self.Operator_Base_Stoppage_Nealit
        super(ProductReport, self).save(*args, **kwargs)
