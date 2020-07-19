from django.urls import path

from . import views

urlpatterns = [
    path('<int:number>/<str:symbol>/<int:number2>', views.index, name='index'),
]