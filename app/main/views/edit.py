from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404
from main.models import (Company)
from main.forms import CompanyForm
from .create import CompanyCreateView

class CompanyEditFormView(View):
    form_class = CompanyForm
    template_name = 'company/company_edit.html'
    def get(self, request, id, *args, **kwargs):
        # getCompany = Company.objects.get(pk=id)
        form =self.form_class(initial={})
        if id is not None:
            obj = get_object_or_404(Company, id=id)
            data = {
                'name': obj.name,
                'address': obj.address,
                'city': obj.city,
                'website': obj.website,
                'countries': obj.country
            }
            print('data', data)
            form = self.form_class(initial=data)
        return render(request, self.template_name, {'form': form, 'id': obj.id ,'option': 'edit'})
    
    def post(self, request, id, *args, **kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            print('this form is working')
            update_company = Company.objects.get(pk=id)
            update_company.name = form.cleaned_data.get('name')
            update_company.address = form.cleaned_data.get('address')
            update_company.country = form.cleaned_data.get('countries')
            update_company.city = form.cleaned_data.get('city')
            update_company.website = form.cleaned_data.get('website')
            update_company.save()
            return HttpResponseRedirect('/company/list/')
        return render(request, self.template_name, {'form': form, 'option': 'edit'})