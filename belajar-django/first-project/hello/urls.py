from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("zakky", views.zakky, name="zakky"),
    path("about", views.about, name="about"),
    path("<str:name>", views.greet, name="greet"),
]
'''
<str:name> berarti semua path selain diatasnya
'''