from django.shortcuts import render

# Create your views here.
def data(request):
    return render(request,'data.html',context={'name':'bhagya','age':22})