# forms.py
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'price', 'location', 'area', 'photo']


class PropertySortForm(forms.Form):
    sort_by = forms.ChoiceField(
        choices=[
            ('', 'Выберите вариант сортировки'),
            ('price', 'По возрастанию цены'),
            ('-price', 'По убыванию цены'),
            ('area', 'По возрастанию площади'),
            ('-area', 'По убыванию площади')
        ],
        required=False,
        label='Сортировать по:'
    )


class PropertyFilterForm(forms.Form):
    min_price = forms.IntegerField(
        required=False,
        label="Минимальная цена"
    )
    
    max_price = forms.IntegerField(
        required=False,
        label="Максимальная цена"
    )
    
    min_area = forms.IntegerField(
        required=False,
        label="Минимальная площадь"
    )
    
    max_area = forms.IntegerField(
        required=False,
        label="Максимальная площадь"
    )