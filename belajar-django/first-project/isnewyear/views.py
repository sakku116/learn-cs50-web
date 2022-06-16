from django.shortcuts import render
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
date = f"{day}-{month}-{year}"

# Create your views here.
def index(request):
    return render(request, "isnewyear/index.html", {
        "isnewyear": month == 1 and day == 1,
        "date": date,
    })
    
def showdate(request):
    print(date) 
    return render(request, "isnewyear/showdate.html", {
        "date": date
    })