from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.



def v1(request):
    if request.method == "POST":
        file1 = request.FILES["photo"]
        print(file1.name)
        fs = FileSystemStorage()
        fs.save(file1.name,file1)
    return render(request, "Images/base.html")

