from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

data = {
    'title': 'Main page!!!!!',
    'values' : ['Some' , 'Hello', '123'],
    'obj' : {
        'car' : 'Volvo',
        'age' : '3',
        'hobby' : 'Football'
    }
}


def index(request):
    #    return HttpResponse("<h4>*****7777</h4>")
    return render(request, "main/index.html",data)


def about(request):
    #    return HttpResponse("<h4>***** page about us</h4>")
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contacts.html")
