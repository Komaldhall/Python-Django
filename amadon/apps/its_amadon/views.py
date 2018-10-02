from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    if not 'sprice' in request.session:
        request.session['sprice']=0
    context={
        'item':Item.objects.all(),
    }
    return render(request, 'its_amadon/index.html', context)

def buy(request):
    if request.POST: 
        print(request.POST)
        con=Item.objects.get(value=request.POST['buy'])
        request.session['sprice']=float(con.price)*float(request.POST['quantity'])   
        Stuff.objects.create(scontent=con.content, sprice=request.session['sprice'],quantity=request.POST['quantity'],charge='Yes' )
        return redirect('/amadon/show')
       
    return redirect('/') 

def show(request):
    context={
        'scontent':request.session['sprice'],
    }
    return render(request, 'its_amadon/checkout.html', context)

