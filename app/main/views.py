from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
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
            return HttpResponseRedirect('/list')
        return render(request, self.template_name, {'form': form, 'option': 'create'})


class CompanyEditFormView(CompanyCreateView):
    
    def get(self, request, *args, **kwargs):
        getCompany = Company.object.get(pk=id)
        form = self.form_class(inital=getCompany)
        return render(request, self.template_name, {'form': form, 'option': 'edit'})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(initial=request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect('/list')
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