from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>", views.entryPage, name="entry-page"),
    path("create-new/", views.createNewPage, name="create-new")
]
