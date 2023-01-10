from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Votre compte a été crée {username}!")
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')