from django.shortcuts import render, HttpResponse, redirect
from random import choice
from string import ascii_uppercase

def index(request):
    request.method =='POST'
    if not 'num' in request.session:
            request.session['num'] = 1
    context={
        'attempt' : request.session['num'],
        'word' : (''.join(choice(ascii_uppercase) for i in range(14)))
    }
    request.session['num']+= 1
    return render(request, "its_rwg/index.html", context)

def reset(request):
    request.session['num'] = 1
    return redirect(index)







