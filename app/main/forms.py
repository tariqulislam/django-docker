from django import forms
from .models import (Company)

COUNTRY = (
    ('BD', 'Bangladesh'),
    ('JP', 'JAPAN')
)

class CompanyForm(forms.ModelForm):
    name= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    countries = forms.CharField(widget=forms.Select(choices=COUNTRY, attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    
    class Meta:
        model = Company
        fields = [
           'name', 'address', 'city', 'website'
        ]

# class EmployeeForm(forms.ModelForm):
#     companies = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label="(No Company)")
#     email = forms.EmailField()
#     address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))

#     class Meta:
#         model = Employee
#         fields = [
#             'first_name', 'last_name', 'email', 'gender', 'phone', 'address', 'company'
#         ]
