# forms.py
from django import forms

class TotalForm(forms.Form):
    total = forms.DecimalField()
