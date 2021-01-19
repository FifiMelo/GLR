from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import models
# Create your views here.



def v1(request):
    counter = models.Counter.objects.first()
    context = {
        "counter": counter.number
    }
    return render(request, "Images/send.html", context=context)

def v2(request):
    if request.method == "POST":
        addition = 0
        fs = FileSystemStorage()
        for file1 in request.FILES.getlist('file'):
            addition += 1
            fs.save(file1.name, file1)
        counter = models.Counter.objects.first()
        counter.number += addition
        counter.save()
    return render(request, "Images/thanks.html")




 

