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

    if request.GET.get('search_food'):
        print('search food name: ',request.GET.get('search_food'))
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search_food'))



    context={'receipes':queryset}

    return render(request,"receipes.html",context=context)


def update_receipes(request,id):
    queryset=Receipe.objects.get(id=id)
    print("queryset:",queryset)
    

    if request.method == 'POST':
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(data)

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipes/')


    
    context={'receipes':queryset}
    print("context: ",context)


    return render(request,"update_receipes.html",context=context)

def delete_receipe(request,id):
    print(id)
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    # return HttpResponse('a')
    return redirect('/receipes/')
