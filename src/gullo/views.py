from django.http import HttpResponse, HttpRequest
from django.shortcuts import render 
from gapp.models import Gapp


def home(request):

    print(request.path)
    about_template = 'user.html'    
    Gapp.objects.create(path=request.path)
    page_count = Gapp.objects.all().count() 
    path_count = Gapp.objects.filter(path=request.path).count()
    percent = ( page_count / path_count ) * 100

    context = {
        
        "page_visits": Gapp.objects.filter(path=request.path).count(),
        'total_visits': Gapp.objects.all().count(),
        "percent": percent,
        "name": "khubaib"
    }
    
    return render(request, "index.html", context)

def about(request, *args, **kwargs):    
        
        about_template = 'user.html'    
        Gapp.objects.create(path=request.path)
        page_count = Gapp.objects.all().count() 
        path_count = Gapp.objects.filter(path=request.path).count()
        percent = ( page_count / path_count ) * 100

        context = {
            "name": "khubaib",
            "page_visits": Gapp.objects.filter(path=request.path).count(),
            'total_visits': Gapp.objects.all().count(),
            "percent": percent,
            "example": "abcd"

        }



        return render(request, "home.html", context)
    

