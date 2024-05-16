from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def receipes(request):
    

    if request.method == 'POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(data)


        print('receipe_name: ',receipe_name)
        print('receipe_description: ',receipe_description)
        print('receipe_image: ',receipe_image)

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image

        )
        return redirect('/receipes')
    
    queryset=Receipe.objects.all()
    context={'receipes':queryset}

    return render(request,"receipes.html",context=context)

def delete_receipe(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    # return HttpResponse('a')
    return redirect('/receipes/')