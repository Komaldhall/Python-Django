from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visitedcopy

#/ - display "placeholder to display all the surveys created" via HttpResponse. Have this be handled by a method named 'index'.
def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)
#/new - display  "placeholder for users to add a new survey" via HttpResponse. Have this be handled by a method named 'new'.    
def new(request):
    response =  "placeholder for users to add a new survey"
    return HttpResponse(response) 










