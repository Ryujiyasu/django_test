from django.shortcuts import render, redirect
from .models import MstPlace, Entry
# Create your views here.
# 20200725 -- start --
# from django.contrib.auth.models import User
# 20200725 -- end --


def index(request):
    places = MstPlace.objects.all()
    # 20200725 -- start --
    # id_name = User.objects.all()
    # 20200725 -- end --
    data = {
        "places": places,
        # 20200725 -- start --
        # "name": id_name
        # 20200725 -- end --
    }

    return render(request, "entry/index.html", data)


def entry(request):
    if request.method == "POST":
        place_id = request.POST["place"]
        place = MstPlace.objects.get(id=place_id)
        Entry.objects.create(
            entry_place=place,
        )

    return redirect("/")


def exit(request):
    if request.method == "POST":
        place_id = request.POST["place"]
        place = MstPlace.objects.get(id=place_id)
        Entry.objects.create(
            exit_place=place,
        )

    return redirect("/")
