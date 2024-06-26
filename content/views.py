from django.shortcuts import render
from .forms import UserRegistrationForm


def main(request):
    return render(request, 'main.html')


def o_nas(request):
    return render(request, 'onas.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'orders/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'orders/register.html', {'form': form})
