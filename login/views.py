from django.shortcuts import render,redirect
from .forms import Signup
from user_account.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

#* SIGN UP USER

def SignUp_User(request):
    frm=Signup(request.POST or None)
    context = {"frm":frm}

    if request.POST:

        print("salam")
        if frm.is_valid():
            print("valid")
            user_type = request.POST.get("user_type")
            data = frm.cleaned_data
            name = data.get("name")
            email = data.get('email')
            password = data.get("password")

            new_user = CustomUser.objects.create(
                username = email,
                first_name = name,
            )

            new_user.set_password(password)

            if user_type == 'user':
                new_user.save()
            elif user_type == 'colleague':
                new_user.save()
                return redirect('/signup/success')

    return render(request,'signup.html',context)

#* SIGN UP USER

#* SUCCESS SIGNUP COLLEAGUE

def Success_Signup(request):
    context = {}
    
    return render(request,'success_signup.html',context)

#* SUCCESS SIGNUP COLLEAGUE

#* LOGOUT VIEW

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/login")
    
    return redirect("/login")

#* LOGOUT VIEW
