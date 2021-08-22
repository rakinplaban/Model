from django import forms
from .models import Stockmarket

class stock_form(forms.ModelForm):
    class Meta:
        model = Stockmarket
        fields = ['trade_code','date','open','close','high','low','volume']

        labels = {
            'trade_code' : 'Trade Code',
            'date' : 'Date',
            'open' : 'Open',
            'close' : 'Close',
            'high' : 'High',
            'low' : 'Low',
            'volume' : 'Volume',
        }

        widgets = {
            'trade_code' : forms.Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Trade Code',
                'rows' : 1,
                'cols' : 100,
                'type' : 'number'
            }),
            'date' : forms.DateInput(attrs={
                'class' : 'form-control',
                'rows' : 1,
                'cols' : 100,
                'type' : 'date'
            }),
            'open' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Open',
                'rows' : 1,
                'cols' : 100,
                'step' : 0.01,
                'type' : 'number'
            }),
            'close' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Close ',
                'rows' : 1,
                'cols' : 100,
                'step' : 0.01,
                'type' : 'number'
            }),
            'high' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'High',
                'rows' : 1,
                'cols' : 100,
                'step' : 0.01,
                'type' : 'number'
            }),
            'low' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Low',
                'rows' : 1,
                'cols' : 100,
                'step' : 0.01,
                'type' : 'number'
            }),
            'volume' : forms.NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Volume',
                'rows' : 1,
                'cols' : 100,
                'step' : 1,
                'type' : 'number'
            }),
        }
