from typing import List

from django import forms
from django.forms import widgets
from .models import Food, Ingredient, DailyMeal


class DailyMealForm(forms.ModelForm):

    class Meta:

        model = DailyMeal
        rice = ['user', 'date', 'time', 'food', 'quantity', 'rice', 'beef', 'lamb', 'chicken_leg', 'chicken_breast']

        fields = rice
        #     (
        #     'user', 'date', 'time', 'food', 'quantity', 'rice', 'beef', 'lamb', 'chicken_leg', 'chicken_breast',
        #     'fish', 'solid_oil', 'liquid_oil', 'beef_shank', 'olive_oil', 'macaroni', 'reshte_poloie', 'rob_anar',
        #     'egg', 'animal_oil', 'butter_1', 'lemon_juice_1', 'butter_bulk', 'tomato_paste', 'lentil', 'raisin',
        #     'walnut', 'split_peas', 'red_beans', 'tomato', 'onion', 'potato', 'broad_bean', 'celery', 'green_bean',
        #     'eggplant', 'amani_lemon', 'lemon', 'sabzi_kuku', 'sabzi_qorme', 'sabzi_poloie', 'garlic', 'bell_pepper',
        #     'mushroom', 'peas', 'coriander', 'dry_savory', 'dried_tarragon', 'spearmint', 'jafari', 'reyhan', 'pickle',
        #     'carrot', 'shevid', 'saffron', 'verjuice', 'lemon_juice', 'white_vinegar', 'white_flour', 'toasted_flour',
        #     'toasted_powder', 'rice_flour', 'chickpea_flour', 'sugar', 'yogurt', 'sumac', 'starch', 'vinegar', 'mustard',
        #     'sauce', 'rosewater', 'barberry', 'rock_salt', 'pepper', 'milk', 'salt',
        # )

        widgets = {
            'user': widgets.Select(),
            'date': widgets.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M:%S' ),
            'time': widgets.TimeInput(attrs={'type': 'time'}, format='%H:%m'),
            'food': widgets.Select(),
            'quantity': widgets.NumberInput(),
            'rice': widgets.NumberInput(),
            'beef': widgets.NumberInput(),
            'lamb': widgets.NumberInput(),
            'chicken_leg': widgets.NumberInput(),
            'chicken_breast': widgets.NumberInput(),
            'fish': widgets.NumberInput(),
            'solid_oil': widgets.NumberInput(),
            'liquid_oil': widgets.NumberInput(),
            'beef_shank': widgets.NumberInput(),
            'olive_oil': widgets.NumberInput(),
            'macaroni': widgets.NumberInput(),
            'reshte_poloie': widgets.NumberInput(),
            'rob_anar': widgets.NumberInput(),
            'egg': widgets.NumberInput(),
            'animal_oil': widgets.NumberInput(),
            'butter_1': widgets.NumberInput(),
            'lemon_juice_1': widgets.NumberInput(),
            'butter_bulk': widgets.NumberInput(),
            'tomato_paste': widgets.NumberInput(),
            'lentil': widgets.NumberInput(),
            'raisin': widgets.NumberInput(),
            'walnut': widgets.NumberInput(),
            'split_peas': widgets.NumberInput(),
            'red_beans': widgets.NumberInput(),
            'tomato': widgets.NumberInput(),
            'onion': widgets.NumberInput(),
            'potato': widgets.NumberInput(),
            'broad_bean': widgets.NumberInput(),
            'celery': widgets.NumberInput(),
            'green_bean': widgets.NumberInput(),
            'eggplant': widgets.NumberInput(),
            'amani_lemon': widgets.NumberInput(),
            'lemon': widgets.NumberInput(),
            'sabzi_kuku': widgets.NumberInput(),
            'sabzi_qorme': widgets.NumberInput(),
            'sabzi_poloie': widgets.NumberInput(),
            'garlic': widgets.NumberInput(),
            'bell_pepper': widgets.NumberInput(),
            'mushroom': widgets.NumberInput(),
            'peas': widgets.NumberInput(),
            'coriander': widgets.NumberInput(),
            'dry_savory': widgets.NumberInput(),
            'dried_tarragon': widgets.NumberInput(),
            'spearmint': widgets.NumberInput(),
            'jafari': widgets.NumberInput(),
            'reyhan': widgets.NumberInput(),
            'pickle': widgets.NumberInput(),
            'carrot': widgets.NumberInput(),
            'shevid': widgets.NumberInput(),
            'saffron': widgets.NumberInput(),
            'verjuice': widgets.NumberInput(),
            'lemon_juice': widgets.NumberInput(),
            'white_vinegar': widgets.NumberInput(),
            'white_flour': widgets.NumberInput(),
            'toasted_flour': widgets.NumberInput(),
            'toasted_powder': widgets.NumberInput(),
            'rice_flour': widgets.NumberInput(),
            'chickpea_flour': widgets.NumberInput(),
            'sugar': widgets.NumberInput(),
            'yogurt': widgets.NumberInput(),
            'sumac': widgets.NumberInput(),
            'starch': widgets.NumberInput(),
            'vinegar': widgets.NumberInput(),
            'mustard': widgets.NumberInput(),
            'sauce': widgets.NumberInput(),
            'rosewater': widgets.NumberInput(),
            'barberry': widgets.NumberInput(),
            'rock_salt': widgets.NumberInput(),
            'pepper': widgets.NumberInput(),
            'milk': widgets.NumberInput(),
            'salt': widgets.NumberInput(attrs={'readonly': 'True'}),
        }

#     def __init__(self, *args, **kwargs):
#         super().__init__( *args, **kwargs )
#         self.fields['quarter'].queryset = Quarter.objects.none()
#
#         if 'hour' in self.data:
#             try:
#                 hour_id = int( self.data.get( 'hour' ) )
#                 self.fields['quarter'].queryset = Quarter.objects.filter( hour_id=hour_id ).order_by( 'hour' )
#             except (ValueError, TypeError):
#                 pass  # invalid input from the client; ignore and fallback to empty City queryset
#         elif self.instance.pk:
#             self.fields['quarter'].queryset = self.instance.hour.quarter_set.order_by( 'quarter' )
#