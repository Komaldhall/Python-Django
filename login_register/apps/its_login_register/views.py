from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import datetime
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
now = datetime.datetime.today().strftime("%Y-%m-%d")


def register(request):
    print(now)
    if request.method == 'POST':
        
        form=request.POST
        errors = []
        print(form['birthday'])
        if len(form['first_name']) < 2:
            errors.append('First name must be at least 2 characters.')
        if len(form['last_name']) < 2:
            errors.append('Last name must be at least 2 characters.')
        if len(form['password']) < 8:
            errors.append('Password must be at least 8 characters.')
        if not form['password'] == form['cpassword']:
            errors.append('Password and password confirmation do not match.')
        # if len(form['email']) < 0:
        #     errors.append('Please provide email')   
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Please provide a valid email') 
        # if len(form['birthday'])<1:
        #     errors.append("Please provide Birth info")
        if form['birthday']>now:
            errors.append("Your birthday refers to a future date. Please check!!")
        
        if errors:
            for e in errors:
                messages.error(request, e)
        else:        
            try:
                User.objects.get(email=form['email'])
                messages.error(request, 'Your email already exists. Please Login.')
            except User.DoesNotExist:
                hashed_pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
                c_hashed_pw = hashed_pw.decode('utf-8')
                birthday=str(form['birthday'])
                # birthday=int(birthday)
                print(birthday)
                User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=c_hashed_pw, birth=birthday)

        
        return redirect('/')
    else:

        return render(request, 'its_login_register/index.html')


def login(request):
    if request.method == 'POST':
        
        errors = []
        form=request.POST
        # if len(form['emaill']) < 0:
        #     errors.append('Please provide email')  
        if not EMAIL_REGEX.match(form['emaill']):
            errors.append('Please provide a valid email') 
        else:
            try:
                user=User.objects.get(email=form['emaill'])
                result = bcrypt.checkpw(request.POST['passwordl'].encode(), user.password.encode())
                if result:
                    request.session['user_id'] = user.id
                    return redirect('/success')
                else:
                    messages.error(request, 'Password does not match.')    
            except User.DoesNotExist:
                messages.error(request, 'Your email does not exists. Please register.')
                return redirect('/')
        
        if errors:
            for e in errors:
                messages.error(request, e)   
        return redirect('/')     

def success(request):
    if not 'user_id' in request.session:
        messages.error(request, 'You need to login.')
        return redirect('/')
    
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user,
    }
    request.session.clear()
    return render(request,'its_login_register/success.html', context)

 

   
        