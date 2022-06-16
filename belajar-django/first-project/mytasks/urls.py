from django.urls import path
from . import views

app_name = "mytasks"
'''
agar tidak terjadi konflik saat menghubungkan page ke page lain dengan nama
url yang sama di dalam app lain.
`href="{%mytasks:[url's name]%}"`
(django logic)
'''

urlpatterns = [
    path("", views.index, name="index"),
    path("addtask", views.addtask, name="addtask")
]