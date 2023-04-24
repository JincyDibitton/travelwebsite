from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Days


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Days.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})

# def about(request):
#     return render(request,'about.html')
#
#
# def contact(request):
#     return HttpResponse('hello Iam contact')
