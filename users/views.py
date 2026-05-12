from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render, redirect
from django.contrib.auth import login

from users.forms import LoginForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('applications')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    return render(
        request,
        'login.html',
        {'form': form}
    )
