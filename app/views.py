from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from app.models import *
from django.conf import settings
import smtplib
# Create your views here.

def usercontact(request):
    if request.method=="POST":
        na=request.POST.get('t1')
        em=request.POST.get('t2')
        # su=request.POST.get('t3')
        ms=request.POST.get('t4')
        # sg=request.POST.get('t5')
        data=contact_tble.objects.create(boardId=na,Name=em,City=ms)
        mail=smtplib.SMTP('smtp.mailgun.org',587)
        mail.ehlo()
        mail.starttls()
        mail.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        message='Hello billboard team..one coustomer has been contacted The BillBoard Id is '+na+' Coustomer Name '+em+ ' and contact number '+ms
        email= 'pratheesh.b123@gmail.com'
        mail.sendmail(settings.EMAIL_HOST_USER,email,message)
        data.save()
        return HttpResponseRedirect(reverse('usercontact'))
    return render(request,"app/ucontact.html")

# def usercontact(request):
#     if request.method=="POST":
#         na=request.POST.get('t1')
#         em=request.POST.get('t2')
#         su=request.POST.get('t3')
#         ms=request.POST.get('t4')
#         data=contact_tble.objects.create(name=na,email=em,subject=su,message=ms)
#         return HttpResponseRedirect(reverse('usercontact'))
#     return render(request,"app/ucontact.html")