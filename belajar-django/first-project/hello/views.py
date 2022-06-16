from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world! from hello app")

def zakky(request):
    return HttpResponse("Hello Zakky!")

def about(request):
    # return response from a file
    # path dimulai dari 'templates'
    return render(request, "hello/about.html")

def greet(request, name):
    #return HttpResponse(f"hello, {name}") # variable dapat langsung diakses jika menggunakan string
    
    return render(request, "hello/greet.html", {
        "name": name
    }) # variable harus melalui dictionary untuk diakses melalui render html file
