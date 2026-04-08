

from django.shortcuts import render, redirect
from .models import User,Role
from .forms import UserForm,RoleForm

def users(request):
    # получим всех пользователей из базы
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):

    if request.method == "POST":

        user = UserForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('/users/')
    else:
        form = UserForm()
    
    return render(request, "add_user.html", {'form': form})

def main(request):
    return render(request, 'base.html', {'page': 'main'})

def add_role(request):
    if request.method == "POST":
        form = RoleForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('/users/')
    else:
        form = RoleForm()
    
    return render(request, "add_role.html", {'form': form})