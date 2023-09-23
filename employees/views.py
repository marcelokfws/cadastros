

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from employees.models import Employee


def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        'employee': employee
    }
    return render(request, 'employee_detail.html', context)


# class SearchResultsView(ListView):
#     model = Employee
#     template_name = "search.html"
