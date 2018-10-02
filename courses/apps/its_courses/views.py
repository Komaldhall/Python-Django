from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    context={
        'course':Course.objects.all(),
    }
    return render(request, 'its_courses/index.html', context)

def add(request):
    if request.POST:     
        errors=[]
        form=request.POST
        if len(form['name'])<3:
            errors.append('Name must be at least 3 characters.')
        if len(form['desc']) < 3:
            errors.append('Please provide description.')
        
        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            Course.objects.create(name=form['name'], desc=form['desc'])  
        print('data added')
    return redirect('/') 

def remove(request,course_id):
    context={
        'course':Course.objects.get(id=course_id) 
    }
    return render(request, 'its_courses/destroy.html', context)
    

def delete(request,course_id):
    course = Course.objects.get(id=course_id) 
    course.delete()
    return redirect('/')