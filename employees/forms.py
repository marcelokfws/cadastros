from django import forms

from employees.models import Employee


class addCadastro(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['photo', 'first_name', 'last_name', 'reds', 'adress']

    widget = {
        'photo': forms.ImageField(),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'reds': forms.TextInput(attrs={'class': 'form-control'}),
        'adress': forms.TextInput(attrs={'class': 'form-control'}),

    }
