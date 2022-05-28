from django.urls import path
from . import views


urlpatterns = [

    path("" , views.inicio),
    path("familiares" , views.familia),
    path("alta_familiares" , views.altaF),



]