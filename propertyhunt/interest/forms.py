from django import forms
from .models import Interest


class MessageForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['text']

        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 30}),
        }

        labels = {
            'text': 'Сообщение',
        }