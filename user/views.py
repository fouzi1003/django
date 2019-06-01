from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
    # return HttpResponse("Hi Welcome.")
    return render(request,'Hello.html', {})


def about(request):
    return render(request,'about.html',{})

def db(request,number):
    # number=input()
    a=[]
    for i in range(0,number):
        a.append(i)
    print(a)   
    return render(request, 'db.html', {'data':a})