from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry_name>/", views.entryPage, name="entry-page"),
    path("wiki/<str:entry_name>/edit/", views.editPage, name="edit-page"),
    path("create-new/", views.createNewPage, name="create-new"),
    path("random-wiki/", views.randomWiki, name="random-wiki"),
]
