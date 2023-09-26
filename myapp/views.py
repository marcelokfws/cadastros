from django.db.models import Q
from django.shortcuts import render

from employees.models import Employee


def home(request):
    employees = Employee.objects.all()
    context = {

        'employees': employees
    }
    return render(request, 'home.html', context)


def search(request):
    Keyword = request.GET.get('Keyword', '')
    employees = Employee.objects.filter(Q(first_name__icontains=Keyword) |
                                        Q(last_name__icontains=Keyword))
    context = {
        'employees': employees}
    return render(request, 'home.html', context)
