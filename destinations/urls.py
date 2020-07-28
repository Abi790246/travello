from django.urls import path

from . import views

urlpatterns = [
    path("hyderbad",views.hyderbad, name="hyderbad"),
    path("bengaluru", views.bengaluru, name="bengaluru"),
    path("mumbai",views.mumbai,name="mumbai"),
    path("delhi",views.delhi,name="delhi"),
    ]