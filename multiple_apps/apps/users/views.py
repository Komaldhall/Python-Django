from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visitedcopy

#/ - display 'placeholder for users to create a new user record' via HttpResponse. Have this be handled by a method named 'index'.
def index(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)
#/new - display "placeholder for users to login" via HttpResponse. Have this be handled by a method named 'new'.    
def new(request):
    response = "placeholder for users to login"
    return HttpResponse(response) 
#/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
def create(request):
    return redirect(index)   
#/{{number}} - display 'placeholder to later display all the list of users'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.    
def show(request):
    response = 'placeholder to later display all the list of users'
    return HttpResponse(response) 









