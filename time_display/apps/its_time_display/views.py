from django.shortcuts import render, HttpResponse, redirect
import datetime
def index(request):
    context = {
       'date':datetime.datetime.now().date(),
       'time':datetime.datetime.now().time()
    }
    return render(request, "its_time_display/index.html", context)