from django.shortcuts import render
import random
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

def index(request,number=1,symbol="+",number2=1):

    if symbol=="+":
        number=number+number2
    elif symbol=="-":
        number = number - number2
    elif symbol == "*":
        number = number * number2
    elif symbol == "%":
        number = number % number2
    elif symbol == "!":
        number = number / number2
    else:
        number=0

    return render(request,"polls/index.html",{
        "message":number,

    })


@login_required
def home(request):


    number=1
    return render(request,"polls/index.html",{
        "message":number,

    })