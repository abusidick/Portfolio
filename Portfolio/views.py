from django.shortcuts import render

def home(request):
    return render(request,'portfolio/home.html')

def about(request):
    return render(request,'portfolio/about.html')

def contact(request):
    return render(request,'porfolio/contact.html')