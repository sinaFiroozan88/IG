from django.db import models


class ProductReport(models.Model):
    day = (
        ("شنبه", 'شنبه'),
        ("یک شنبه", 'یک شنبه'),
        ("دو شنبه", 'دو شنبه'),
        ("سه شنبه", 'سه شنبه'),
        ("چهار شنبه", 'چهار شنبه'),
        ("پنج شنبه", 'پنج شنبه'),
        ('چمعه', 'جمعه')
    )
    day = models.CharField(blank=True, null=True, choices=day, max_length=99999999)
    # crasher operation
    Machinery = models.TimeField()
    Crasher_Elec_Consumption = models.IntegerField()
    No_Needed = models.TimeField()
    Electrical_Fault = models.TimeField()
    Mechanical_Fault = models.TimeField()
    Operator_Fault = models.TimeField()
    Total_Fault = models.IntegerField(editable=False)
    # Raw Material Consumption
    Kenaf_Rawmat_Consumption = models.IntegerField(max_length=4)
    Kenaf_Stucco_Prod_1 = models.IntegerField(max_length=4)
    Kenaf_Stucco_Prod_2 = models.IntegerField(max_length=4)
    Ordinary_RawMat_Consumption_1 = models.IntegerField(max_length=4)
    Ordinary_RawMat_Consumption_2 = models.IntegerField(max_length=4)
    Ordinary_Stucco_Prod_1 = models.IntegerField(max_length=4)
    Ordinary_Stucco_Prod_2 = models.IntegerField(max_length=4)
    Block_RawMat_Consumption_1 = models.IntegerField(max_length=4)
    Block_RawMat_Consumption_2 = models.IntegerField(max_length=4)
    Nealit_RawMat_Consumption = models.IntegerField(max_length=4)
    Nealit_Sugar_Consumption = models.IntegerField(max_length=4)
    Nealit_Prod = models.IntegerField(max_length=4)
    Total_Consumption = models.IntegerField(editable=False)
    Total_Prod = models.IntegerField(editable=False)
    # stoppage causes
    No_Needed_1 = models.TimeField()
    No_Needed_2 = models.TimeField()
    No_Needed_Nealit = models.TimeField()
    Electrical_Stoppage_1 = models.TimeField()
    Electrical_Stoppage_2 = models.TimeField()
    Electrical_Stoppage_Nealit = models.TimeField()
    Mechanical_Stoppage_1 = models.TimeField()
    Mechanical_Stoppage_2 = models.TimeField()
    Mechanical_Stoppage_Nealit = models.TimeField()
    Blackout_Stoppage_1 = models.TimeField()
    Blackout_Stoppage_2 = models.TimeField()
    Blackout_Stoppage_Nealit = models.TimeField()
    Gas_Cutout_Stoppage_1 = models.TimeField()
    Gas_Cutout_Stoppage_2 = models.TimeField()
    Gas_Cutout_Stoppage_Nealit = models.TimeField()
    Gasoil_Cutout_Stoppage_1 = models.TimeField()
    Gasoil_Cutout_Stoppage_2 = models.TimeField()
    Gasoil_Cutout_Stoppage_Nealit = models.TimeField()
    Initial_Start_Stoppage_1 = models.TimeField()
    Initial_Start_Stoppage_2 = models.TimeField()
    Initial_Start_Stoppage_Nealit = models.TimeField()
    End_production_Stoppage_1 = models.TimeField()
    End_production_Stoppage_2 = models.TimeField()
    End_production_Stoppage_Nealit = models.TimeField()
    Operator_Base_Stoppage_1 = models.TimeField()
    Operator_Base_Stoppage_2 = models.TimeField()
    Operator_Base_Stoppage_Nealit = models.TimeField()
    Total_Stoppage_1 = models.TimeField()
    Total_Stoppage_2 = models.TimeField()
    Total_Stoppage_Nealit = models.TimeField()
    # silo inventories
    Silo_1_Inventory = models.IntegerField(max_length=4)
    Silo_2_Inventory = models.IntegerField(max_length=4)
    Block_Silo_N_Inventory = models.IntegerField(max_length=4)
    Block_Silo_S_Inventory = models.IntegerField(max_length=4)
    Silo_800_Inventory = models.IntegerField(max_length=4)
    # energy consumption
    Gas_Consumption_AM_1 = models.IntegerField(max_length=4)
    Gas_Consumption_PM_1 = models.IntegerField(max_length=4)
    Gas_Consumption_AM_2 = models.IntegerField(max_length=4)
    Gas_Consumption_PM_2 = models.IntegerField(max_length=4)
    Gasoil_Consumption_AM_1 = models.IntegerField(max_length=4)
    Gasoil_Consumption_PM_1 = models.IntegerField(max_length=4)
    Gasoil_Consumption_AM_2 = models.IntegerField(max_length=4)
    Gasoil_Consumption_PM_2 = models.IntegerField(max_length=4)
    Gas_Temperature_1 = models.IntegerField(max_length=4)
    Gas_Temperature_2 = models.IntegerField(max_length=4)
    Gas_Presure_1 = models.IntegerField(max_length=4)
    Gas_Presure_2 = models.IntegerField(max_length=4)
