from django.shortcuts import render

# Create your views here.
def mainpage(request):
    context={}
    return render(request,'store/main.html',context)