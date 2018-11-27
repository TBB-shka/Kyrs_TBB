"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
from datetime import datetime
from app.models import Product



        

def shable(request):
    return render(request,'app/Shablyan.html')



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def data(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Data.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def vidod(request):
    print(request)
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/vivod.html',
        {
        }
    )

def Table():
    a=1
    while a<10:
        a=a+1
        b=str(a)
        c = Product(name='Name '+b, price='Price '+b,link='Link '+b)
        c.save()
        print(c.name + ' ' + c.price+' '+c.link)
    print('все !!! ')
    print(' ')
    for p in Product.objects.raw('SELECT * FROM app_product'):
        print(p)
   
    # al = Product.obects.all()
   # print(al)


def search(request):    
    if 'q' in request.GET:
        tre=str(request.GET['q'])
        print(tre)
        #print(request)
        message = 'You searched for: %r' % request.GET['q']+' Yes'

    else:
         if 'q' in request.GET and 't' =="no":
            #print(request)
            message = 'You searched for: %r' % request.GET['q']+' No'
         else:
            message = 'You submitted an empty form.'
    tre='!'
    for p in Product.objects.raw('SELECT * FROM app_product'):
        tre=tre + p.name
    
        # работа с возвращением # 

   # response = HttpResponse()
   # response.write('{%extends "app/Shablya2.html"%}\n')
   # response.write('{% block contant %}\n')
   # response.write('{%include "app/include/include.html"%}\n')
   # response.write('{%endblock%}')
   # 
   # response.write("<h2>Хууууй</h2>\n")
   # response.write("<p>Here's the text of the Web page.</p>\n")   
   # response.write('{%include "app/include/include.html"%}\n')
    return HttpResponse(tre)








from .forms import Data

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Data(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Data()

    return render(request, 'Data.html', {'form': form})