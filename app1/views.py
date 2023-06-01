from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    return render(request,'login.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')



