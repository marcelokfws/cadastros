from django.contrib import messages
from django.shortcuts import redirect, render

from .admin import CustomUserCreationForm


# Create your views here.
def register(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_valid = False
            user.save()
            messages.success(
                request, 'Registrado. Agora faça o login para começar!')
            return redirect('mysite')

        else:
            print('invalid registration details')

    return render(request, "registration/register.html", {"form": form})
