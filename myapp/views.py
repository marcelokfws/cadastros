
from django.db.models import Q
from django.shortcuts import redirect, render

from employees.forms import addCadastro
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


def add_cadastro(request):
    form = None
    if request.method == 'POST':
        form = addCadastro(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            print('Form not valid')
            return redirect('home')
        print('Form not valid')
    else:
        form = addCadastro()
    return render(request, 'add_cadastro.html', {'form': form})
