from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import pyshorteners


def index(request, **kwargs):
    if request.user.is_authenticated == True:
        present_user = request.user.username 
        if request.method == 'POST':
            try:
                link = request.POST.get('longurl')
                print(link)
                shortener = pyshorteners.Shortener()
                finalurl = shortener.tinyurl.short(link)
                shorturlvalue = finalurl
                data = {'shorturlvalue':shorturlvalue}
                URLRedirection(profile_username = present_user, shortURL = finalurl, longURL =link ).save()
                return render(request, "index.html", data)
            except:
                shorturlvalue = ""
                data = {'shorturlvalue':shorturlvalue}
                return render(request, "index.html", data)
        else:
            shorturlvalue = ""
            data = {'shorturlvalue':shorturlvalue}
            return render(request, "index.html", data)
    else:
        return render(request, "index.html")

def myurls(request):
    if request.user.is_authenticated == True:
        present_user = request.user.username
        urldetails = URLRedirection.objects.filter(profile_username = present_user)
        data = {'urldetails' : urldetails}
        return render(request, 'myurls.html',data)
    else:
        return redirect('/authenticate/login')