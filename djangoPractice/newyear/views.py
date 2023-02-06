from datetime import datetime

from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.now()
    month = now.month
    day = now.day
    return render(request, "newyear/index.html", 
    {
        "newyear": month == 1 and day == 1
    })