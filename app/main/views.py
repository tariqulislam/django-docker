from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from .forms import CompanyForm, EmployeeForm


class CompanyListView(View):
    template_name = 'list.html'

class CompanyView(View):
    form_class = CompanyView
    inital = {}
    template_name = 'company.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.inital)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success')
        return render(request, self.template_name, {'form': form})

class EmployeeListView(View):
    form_class = EmployeeForm
    initial = {}
    template_name = 'list.html'

class EmployeeFormView(View):
    form_class = EmployeeForm
    initial = {}
    template_name = 'employee.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=initial)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        if form.is_valid():
            return HttpResponseRedirect('/success')
        return render(request, self.template_name, {'form': form})