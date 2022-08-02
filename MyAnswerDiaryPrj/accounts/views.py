from django.shortcuts import redirect, render
from django.contrib import auth
from .models import UserModel

def signup(request):
    if request.method == "POST":
        user_id = request.POST.get('id', '')
        user_pw = request.POST.get('pw', '')
        user_pw_confirm = request.POST.get('pw-confirm', '')
        user_name = request.POST.get('name', '')

        if (user_id or user_pw or user_pw_confirm or user_name) == "":
            return render(request, 'bad_blank.html')
        elif user_pw != user_pw_confirm:
            return render(request, 'bad_password.html')
        else:
            user = UserModel(
            user_id = user_id,
            user_pw = user_pw,
            user_name = user_name
            )
            user.save()
        return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return redirect('main')
