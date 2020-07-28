from django.urls import path

from . import views
urlpatterns=[
    path('contact',views.contact,name="contact"),
    path('news',views.news,name="news"),
    path('about',views.about,name="about"),
]