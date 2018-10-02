from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if not 'students' in request.session:
        request.session['students'] = []
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, "its_survey_form/index.html")

def process(request):          
    request.method=='POST'
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['message']=request.POST['message']
    request.session['count']+=1
    return redirect (result)    
        
def result(request):
    
    return render(request, "its_survey_form/result.html")









    