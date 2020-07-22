from django.shortcuts import render,redirect
from .models import MstPlace,Entry
# Create your views here.


def index(request):
    places= MstPlace.objects.all()

    data={
        "places":places
    }
    return render(request,"entry/index.html",data)


def entry(request):
    if request.method=="POST":
        place_id = request.POST["place"]

        place = MstPlace.objects.get(id=place_id)

        Entry.objects.create(
            entry_place=place,
        )

    return redirect('/')