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

    subject = "題名"
    message = "本文ですこんにちは。メールを送信しました"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [
        "ryuji.yasu@gmail.com"
    ]

    send_mail(subject, message, from_email, recipient_list)
    number=1
    return render(request,"polls/index.html",{
        "message":number,

    })