from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visitedcopy

#/ - display "placeholder to later display all the list of blogs" via HttpResponse. Have this be handled by a method named 'index'.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
#/new - display "placeholder to display a new form to create a new blog" via HttpResponse. Have this be handled by a method named 'new'.    
def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response) 
#/create - Have this be handled by a method named 'create'.  For now, have this url redirect to /.
def create(request):
    return redirect(index)   
#/{{number}} - display 'placeholder to display blog {{number}}'.  For example /15 should display a message 'placeholder to display blog 15'.  Have this be handled by a method named 'show'.    
def show(request, number):
    response = 'placeholder to display blog'
    return HttpResponse(response+' '+number) 
#/{{number}}/edit - display 'placeholder to edit blog {{number}}.  Have this be handled by a method named 'edit'. 
def edit(request, number):
    response = 'placeholder to edit blog'
    return HttpResponse(response+' '+number)  
#/{{number}}/delete - Have this be handled by a method named 'destroy'. For now, have this url redirect to /.   
def destroy(request, number):
    return redirect(index) 










