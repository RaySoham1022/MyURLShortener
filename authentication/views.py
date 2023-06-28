from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from home_page.models import *

def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        cnfpassword = request.POST.get("cnfpassword")
        username = email.split('@')[0]


        if User.objects.filter(email=email).exists():
            messages.info(request, "*Email already exists !!")
            return redirect("/authenticate/signup/")
        elif password != cnfpassword :
            messages.info(request, "Conirm Password doesn't Match")
            return redirect("/authenticate/signup/")
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            messages.success(request, "Succesfully Registered !!")
            response = redirect("/authenticate/login")
            return response
    else:
        return render(request, "signup.html")


def login(request, **kwargs):
    email = request.POST.get("email")
    password = request.POST.get("password")
    if request.method == "POST":
        usernames = email.split('@')[0]
        user = auth.authenticate(username=usernames, password=password)
        if user is not None:
            request.session["uid"] = email
            auth.login(request, user)
            login_data = {"my_user": usernames}
            response = redirect("/", kwargs=login_data)
            if request.POST.get("remember_me"):
                response.set_cookie("cid", email)
                response.set_cookie("cid2", password)
                return response
            else:
                return response

        else:
            messages.info(request, "Invalid Credentials !!")
            return redirect("/authenticate/login")
    else:
        if request.COOKIES.get("cid"):
            my_cookie = {
                "usercookie": request.COOKIES["cid"], "passcookie": request.COOKIES["cid2"]}
            return render(request, "login.html", my_cookie)
        else:
            return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")