from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):

    if request.method=="POST":
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        return HttpResponse('Topic name inserted sucessfully')


    return render(request, 'insert_topic.html')


def insert_webpage(request):
    
    if request.method=="POST":
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        # TO.save()

        n=request.POST['n']
        e=request.POST['e']
        u=request.POST['u']
        WO=Webpage.objects.get_or_create(topic_name=TO, name=n, email=e, url=u)[0]
        WO.save()

        return HttpResponse('Webpage inserted sucessfully')

    return render(request, 'insert_webpage.html')


def insert_access(request):

    if request.method=="POST":
        tn=request.POST['tn']
        TO=Topic.objects.get(topic_name=tn)
        # TO.save()

        n=request.POST['n']
        WO=Webpage.objects.get(name=n)
        # WO.save()

        a=request.POST['a']
        d=request.POST['d']
        AO=AccessRecord.objects.get_or_create(name=WO, author=a, date=d)[0]
        AO.save()

        return HttpResponse('AccessRecord inserted sucessfully')
    

    return render(request, 'insert_access.html')
