from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser
from .forms import AddGif
from .models import Gif


# Create your views here.
def index(request):
    all_gifs = Gif.objects.all()
    return render(request, 'index.html',{'Gifs': all_gifs})

def view_gif(request,):
    obj = Gif.objects.all().order_by('-id')  
    return render(request, 'view_gif.html',{'Gifss': obj})

def add_gif(request):

    if request.method == "GET":
        form = AddGif()
        return render(request, 'add_gif.html', {'form':form})

    if request.method == 'POST':
    
        # POST, generate form with data from the request
        form = AddGif(request.POST)
        # check if we get data
        # print("data", form.data)
        # check if it's valid:
        if form.is_valid():
            uploader_name=form.cleaned_data['uploader_name']
            title =form.cleaned_data['title']
            url =form.cleaned_data['url']

            a1 = Gif(uploader_name=uploader_name, title=title, url=url)
            a1.save()
            
            # print the values to make sure their are correct
            return render(request, 'add_gif.html')
        else:
             # print the errors, just in case
            print("---ERRORS---", form.errors)
            return render(request, 'add_gif.html')

    else:
        # GET, generate blank form
        return render(request, 'add_gif.html',{'form':form})




















        


    