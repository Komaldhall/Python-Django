from django.shortcuts import render, HttpResponse, redirect
import datetime
import random

def index(request):
    if not 'building' in request.session:
        request.session['building']=""
    if not 'gold' in request.session:
        request.session['gold']=0
    if not 'num' in request.session:
        request.session['num']=0   
    if not 'activities' in request.session:
        request.session['activities']=[]  
    print(request.session['activities'])  

    return render(request, "its_ninja_gold/index.html")

def process(request):
    request.method==['POST']
    if request.POST['building']=="farm":
        number=random.randint(10,21)
        request.session['gold']+=number
        
    elif request.POST['building']=="cave":
        number=random.randint(5,11)
        request.session['gold']+=number
    elif request.POST['building']=="house":
        number=random.randint(2,6)
        request.session['gold']+=number
    elif request.POST['building']=="casino":
        number=random.randint(-50,51)
        request.session['gold']+=number  

    if request.session['gold']<0:
        request.session['gold']=0
    if number>0:
        num_dict={ 
            'message':"Earned {} golds from the {}.".format(number,request.POST['building']),
            'type':'success'
            }
        
    elif number<0:
        num_dict={ 
            'message':"lost {} golds from the {}.".format(-number,request.POST['building']),
            'type':'failure'
            }  

    request.session['activities'].append(num_dict)
    

       
    return redirect(index)

def clear(request):
    request.session.clear()

    return redirect('/')




