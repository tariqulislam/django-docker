from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, get_object_or_404
from main.models import (Company)


class CompanyListView(View):
    template_name = 'company/company_list.html'
    initial_data = {}
    def get(self, request, *args, **kwargs):
        initial_data = Company.objects.all()
        return render(request, self.template_name, {'company_list': initial_data})