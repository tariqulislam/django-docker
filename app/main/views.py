from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import (Company)
from .forms import CompanyForm


class CompanyListView(View):
    template_name = 'company/company_list.html'
    initial_data = {}
    def get(self, request, *args, **kwargs):
        initial_data = Company.objects.all()
        return render(request, self.template_name, {'company_list': initial_data})
        

class CompanyDetailsView(View):
    template_name = 'comapny/company.html'
    initial_data = {}

    def get(self, request, *args, **kwargs):
        initial_data = Company.objects.get(pk=id)
        return render(request, self.template_name, {'company': initial_data})

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

# class EmployeeListView(View):
#     form_class = EmployeeForm
#     initial = {}
#     template_name = 'employee/employee_list.html'

# class EmployeeCreateFormView(View):
#     form_class = EmployeeForm
#     initial = {}
#     template_name = 'employee/employee_edit.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=initial)
#         return render(request, self.template_name, {'form': form})
    
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         if form.is_valid():
#             return HttpResponseRedirect('/success')
#         return render(request, self.template_name, {'form': form})

# class EmployeeEditFormView(EmployeeCreateFormView):
    
#     def get(self, request, id, *args, **kwargs):
#         form = self.form_class(request)
    
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(initial=request.POST)
        
#         if form.is_valid():
#             return HttpResponseRedirect('/success')
#         return render(request, self.template_name, {'form': form})