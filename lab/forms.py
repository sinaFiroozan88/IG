from django import forms
from .models import Lab
from general.models import Hour, Quarry, Quarter
# from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from django.forms import widgets
from django.core.validators import MinValueValidator, MaxValueValidator
# from durationwidget.widgets import TimeDurationWidget


# from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
# from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime


class LabForm(forms.ModelForm):
    class Meta:
        model = Lab
        # duration = forms.DurationField(widget=TimeDurationWidget(show_days=True, show_hours=True, show_minutes=True, show_seconds=True), required=False )
        fields = {'created_date', 'hour','quarter', 'line', 'mine', 'einstrumenge', 'initial_setting_time', 'final_setting_time',
                  'crystal_water_rawmat', 'purity_rm', 'crystal_water_stucco', 'water_gypsum_ratio',
                  'retained_63_micron',
                  'retained_200_micron', 'retained_500_micron', 'soluble_anhydrite', 'hemihydrate',
                  'low_solubility_anhydrite',
                  'non_conformity', 'nonconf_P6', 'nonconf_P5', 'nonconf_P2', 'nonconf_IS', 'nonconf_FS', 'nonconf_EI',
                  'nonconf_FM', 'nonconf_CS', 'action', 'remarks', 'product_silo', 'published_date', 'free_moisture',
                  'author',
                  'burner_sp_change', 'call_to_operator', }
        widgets = {
            'created_date': widgets.DateInput(attrs={'type': 'date'}),
            # 'created_date': AdminJalaliDateWidget(),
            # https://stackoverflow.com/questions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
            # 'published_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S' ),
            'published_date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S' ),
            # 'published_date': widgets.TimeInput(attrs={'type': 'time', min:"12:00", max:"18:00"}, format='%H:%m'),

            # start = forms.DateTimeField(
            # input_formats=['%Y-%m-%dT%H:%M'],
            # widget=forms.DateTimeInput(
            #     attrs={
            #         'type': 'datetime-local',
            #         'class': 'form-control'},
            #     format='%Y-%m-%dT%H:%M' )
        # )

                      # widgets.DateTimeInput( attrs={
                      #     'type': 'datetime-local',
                      #     'class': 'form-control'
                      # }, format='%Y-%m-%dT%H:%M' ),
            # 'initial_setting_time': widgets,
            # 'initial_setting_time': TimeDurationWidget(show_days=False, show_hours=False, show_minutes=True, show_seconds=True),
            # 'final_setting_time': TimeDurationWidget(show_days=False, show_hours=False, show_minutes=True, show_seconds=True),
            # https://pypi.org/project/django-durationwidget/s
            'einstrumenge': widgets.NumberInput(),
            'retained_63_micron': widgets.NumberInput(),
            'retained_200_micron': widgets.NumberInput(),
            'retained_500_micron': widgets.NumberInput(),
            # 'crystal_water_rawmat': widgets.NumberInput(attrs={'style': 'width:60px'}),
            'crystal_water_stucco': widgets.NumberInput(),
            'soluble_anhydrite': widgets.NumberInput(),
            'hemihydrate': widgets.NumberInput(),
            'low_solubility_anhydrite': widgets.NumberInput(),
            'mine': widgets.Select(),
            'line': widgets.Select(),
            'hour': widgets.Select(),
            'quarter': widgets.Select(),
            'action': widgets.Select(),
            # 'purity_rm': widgets.NumberInput(attrs={'style': 'width:60px', 'disabled':'disabled'}),
            'product_silo': widgets.Select(),
            'water_gypsum_ratio': widgets.NumberInput(),
            'remarks': widgets.Textarea(),
            'burner_sp_change': widgets.NumberInput(),
            'call_to_operator': widgets.Select(),
            'free_moisture': widgets.NumberInput(),
            'non_conformity': widgets.CheckboxInput(),
            'crystal_water_rawmat': widgets.NumberInput(),
            'purity_rm': widgets.NumberInput(attrs={'readonly': 'True'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs )
        self.fields['quarter'].queryset = Quarter.objects.none()

        if 'hour' in self.data:
            try:
                hour_id = int( self.data.get( 'hour' ) )
                self.fields['quarter'].queryset = Quarter.objects.filter( hour_id=hour_id ).order_by( 'hour' )
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['quarter'].queryset = self.instance.hour.quarter_set.order_by( 'quarter' )



#     class Meta:
#         model = TagCat
#
# class MyAdmin(admin.ModelAdmin):
#     fields = ['name', 'by_admin']
#     form = MyAdminForm
