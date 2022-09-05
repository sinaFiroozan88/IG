from django import forms
from django.forms import widgets
from .models import ProductModel


class Product_Form(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = {
            'line', 'year', 'month', 'day', 'hour', 'author', 'main_product', 'quarry', 'kiln_feed_tonnage', 'gas_valve_sp',
            'kiln_inlet_temp', 'setpoint_temp', 'kiln_outlet_temp', 'filter_fan_frequency', 'kiln_amper',
            'kiln_negative_presure', 'stucco_temperature',
            'saparator_frequency', 'moleculator_N_frequency', 'moleculator_S_frequency', 'gas_counter_digit',
            'energy_consumption', 'silo800_feed_time',
            'silo_knauf_1_feed_time', 'silo_knauf_2_feed_time', 'silo_block_1_feed_time', 'silo_block_2_feed_time',
            'silo_emergency_1_feed_time',
            'silo_emergency_2_feed_time', 'work_without_output', 'stoppage', 'stoppage_cause',
            'product_deviation_cause', 'description'
        }
        widgets = {
            'line': widgets.Select(),
            'year': widgets.NumberInput(),
            'month': widgets.NumberInput(),
            'day': widgets.NumberInput(),
            'hour': widgets.NumberInput(),
            'author': widgets.Select(),
            'main_product': widgets.Textarea(),
            'quarry': widgets.Select(),
            'kiln_feed_tonnage': widgets.NumberInput(),
            'gas_valve_sp': widgets.NumberInput(),
            'kiln_inlet_temp': widgets.NumberInput(),
            'setpoint_temp': widgets.NumberInput(),
            'kiln_outlet_temp': widgets.NumberInput(),
            'filter_fan_frequency': widgets.NumberInput(),
            'kiln_amper': widgets.NumberInput(),
            'kiln_negative_presure': widgets.NumberInput(),
            'stucco_temperature': widgets.NumberInput(),
            'saparator_frequency': widgets.NumberInput(),
            'moleculator_N_frequency': widgets.NumberInput(),
            'moleculator_S_frequency': widgets.NumberInput(),
            'gas_counter_digit': widgets.NumberInput(),
            'energy_consumption': widgets.NumberInput(),
            'silo800_feed_time': widgets.NumberInput(),
            'silo_knauf_1_feed_time': widgets.NumberInput(),
            'silo_knauf_2_feed_time': widgets.NumberInput(),
            'silo_block_1_feed_time': widgets.NumberInput(),
            'silo_block_2_feed_time': widgets.NumberInput(),
            'silo_emergency_1_feed_time': widgets.NumberInput(),
            'silo_emergency_2_feed_time': widgets.NumberInput(),
            'work_without_output': widgets.NumberInput(),
            'stoppage': widgets.NumberInput(),
            'stoppage_cause': widgets.Select(),
            'product_deviation_cause': widgets.Textarea(),
            'description': widgets.Textarea(),
        }
