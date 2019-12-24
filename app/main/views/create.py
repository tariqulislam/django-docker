from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404
from main.models import (Company)
from main.forms import CompanyForm

class CompanyCreateView(View):
    form_class = CompanyForm
    inital = {}
    template_name = 'company/company_edit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.inital)
        return render(request, self.template_name, {'form': form, 'option': 'create'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            print(request.POST)
            new_company = Company()
            new_company.name = form.cleaned_data.get('name')
            new_company.address = form.cleaned_data.get('address')
            new_company.country = form.cleaned_data.get('countries')
            new_company.city = form.cleaned_data.get('city')
            new_company.website = form.cleaned_data.get('website')
            new_company.save()
            return HttpResponseRedirect('/company/list/')
        return render(request, self.template_name, {'form': form, 'option': 'create'})