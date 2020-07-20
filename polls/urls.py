from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('<int:number>/<str:symbol>/<int:number2>', views.index, name='index'),
    path('', views.home, name='home'),
]