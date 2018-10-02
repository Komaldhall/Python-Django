from django.shortcuts import render, HttpResponse, redirect
import datetime

def index(request):
    
    if not 'new_word' in request.session:
        request.session['new_word']=[]
    if not 'col' in request.session:
        request.session['col']=""   
   
    
    return render(request, "its_session_words/index.html")


def add_word(request):
    request.method==['POST']
    if 'font' in request.POST:
        request.session['font'] = 1
    else:
        request.session['font']=0
    date = datetime.datetime.now()
    
    new_dict={
        'date':date.strftime("%Y-%m-%d %H:%M"),
        'time':str(date.time()),
        'word':request.POST['word'],
        'color':request.POST['color'],
        'font':request.session['font']
        }
    if new_dict['font']==1:
        new_dict['word'] = new_dict['word'].upper()
    request.session['new_word'].append(new_dict)
    return redirect(index)

def clear(request):       
    request.session.clear()
    
    return redirect(index)