from django import forms
from .models import (Company,Employee)

COUNTRY = (
    ('BD', 'Bangladesh'),
    ('JP', 'JAPAN')
)

class CompanyForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    conutries = forms.CharField(widget=forms.Select(choices=COUNTRY))
    class Meta:
        model = Company
        fields = [
            'name', 'address', 'country', 'city', 'website'
        ]

class EmployeeForm(forms.ModelForm):
    companies = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="(No Company)")
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

    class class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'gender', 'phone', 'address', 'company'
        ]
