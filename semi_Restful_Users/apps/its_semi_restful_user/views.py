from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



def index(request):
    # if not 'user' in request.session:
    #     request.session['user']=0
    context={
        'user':Users.objects.all(),
    }
    print(context)
    return render(request, 'its_semi_restful_user/index.html', context)
    # return render(request, 'its_semi_restful_user/new_user.html')

def add(request):
    if request.POST:
        errors=[]
        print(request.POST)
        form=request.POST
        if len(form['first_name'])<3:
            errors.append('First name must be at least 3 characters.')
        if len(form['last_name']) < 3:
            errors.append('Last name must be at least 3 characters.')
        if len(form['email']) < 0:
            errors.append('Please provide email')   
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Please provide a valid email')  


        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            Users.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'])                   
        
            print('data saved')

    return render(request, 'its_semi_restful_user/new_user.html')
    
def show(request, user_id):
    
    user = Users.objects.get(id=user_id) 
    context={
        'user':user,
    }
    request.session['user']=user_id
    return render(request, 'its_semi_restful_user/show_user.html', context)

    
def delete(request, user_id):
    user = Users.objects.get(id=user_id) 
    user.delete()
    return redirect('/users')

def edit(request,user_id): 
    context={   
        'user':Users.objects.get(id=user_id),
    }
    
#     return render(request, 'its_semi_restful_user/edit_user.html', context)

# def update(request, user_id):
    if request.POST:
        errors=[]
        print(request.POST)
        form=request.POST
        if len(form['first_name'])<3:
            errors.append('First name must be at least 3 characters.')
        if len(form['last_name']) < 3:
            errors.append('Last name must be at least 3 characters.')
        if len(form['email']) < 0:
            errors.append('Please provide email')   
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Please provide a valid email')  


        if errors:
            for e in errors:
                messages.error(request, e)
        else:
            user=Users.objects.get(id=user_id)
            user.first_name=form['first_name']
            user.last_name=form['last_name']
            user.email=form['email']
            user.save()
            return redirect('/users')
    return render(request, 'its_semi_restful_user/edit_user.html', context)




   


