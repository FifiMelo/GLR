from django.shortcuts import render

# Create your views here.



def v1(request):
    print(request)
    return render(request, "Images/base.html")