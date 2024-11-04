# forms.py
from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name',
            'price', 
            'location',
            'area',
            'photo',
            'description'
        ]
        labels = {
            'name': 'Название',
            'price': 'Цена',
            'location': 'Местоположение',
            'area': 'Площадь',
            'photo': 'Фото',
            'description': 'Описание(не более 500 символов)',
        }


class PropertySortAndFilterForm(forms.Form):
    sort_by = forms.ChoiceField(
        choices=[
            ('', 'Sort by:'),
            ('price', 'Price: low to high'),
            ('-price', 'Price: high to low'),
            ('area', 'Area: Small to Large'),
            ('-area', 'Area: Large to Small'),
        ],
        required=False,
        label='Sort by:',
    )

    min_price = forms.IntegerField(
        required=False,
        label="Min price"
    )
    
    max_price = forms.IntegerField(
        required=False,
        label="Max price"
    )
    
    min_area = forms.IntegerField(
        required=False,
        label="Min area"
    )
    
    max_area = forms.IntegerField(
        required=False,
        label="Max area"
    )
