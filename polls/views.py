from django.shortcuts import render
import random
from django.http import HttpResponse


def index(request,number,symbol,number2):

    if symbol=="+":

        number=number+number2
    elif symbol=="-":
        number = number - number2
    else:
        number=0


    return render(request,"polls/index.html",{
        "message":number,

    })