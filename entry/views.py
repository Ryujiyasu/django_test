from django.shortcuts import render, redirect
from .models import MstPlace, Entry
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# 20200725 -- start --
# from django.contrib.auth.models import User
# 20200725 -- end --

@login_required
def index(request):
    try:
        entry = Entry.objects.get(user=request.user, exit_date__isnull=True)
        places = MstPlace.objects.all()
        data = {
            "entry": entry,
            "entry_flg": True,
            "places": places,
        }
        return render(request, "entry/index.html", data)
    except:
        places = MstPlace.objects.all()
        data = {
            "places": places,
            "enrty_flg": False,
        }
        return render(request, "entry/index.html", data)
    return redirect("/")


@login_required
def entry(request):
    if request.method == "POST":
        place_id = request.POST["place"]
        place = MstPlace.objects.get(id=place_id)
        entry = Entry.objects.create(
            user=request.user,
            entry_place=place,
        )

        places = MstPlace.objects.all()
        data = {
            "entry": entry,
            "entry_flg": True,
            "places": places,
        }
        return render(request, "entry/index.html", data)
    return redirect("/")


@login_required
def exit(request):
    if request.method == "POST":
        place_id = request.POST["place"]
        entry_id = request.POST["entry_id"]
        place = MstPlace.objects.get(id=place_id)
        entry = Entry.objects.get(id=entry_id, user=request.user)
        entry.exit_place = place
        entry.exit_date = timezone.now()
        entry.save()

    return redirect("/")

#
#import requests
#data={
#   "id":1,
#   "place_id":2
#   }
#requests.post("http://127.0.0.1:8000/api",data)
#
#


@csrf_exempt
def api(request):
    if request.method == "POST":
        id = request.POST["id"]
        place_id = request.POST["place_id"]
        user = User.objects.get(id=id)
        place = MstPlace.objects.get(id=place_id)
        Entry.objects.create(
            user=user,
            entry_place=place,
        )
        return HttpResponse("登録完了")
