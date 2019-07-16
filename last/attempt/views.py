from django.shortcuts import render,redirect

from django.http import HttpResponse

from .serializer import signupserializer

from rest_framework. renderers import JSONRenderer

from rest_framework.views import APIView

from rest_framework .response import Response

from .forms import Loginform

from .forms import signupform

import random

from . models import city

from . models import country

from  . models import User

from django.core.mail import send_mail

from django.conf import settings

from .models import city

#from .models import country

import http

import json



# Create your views here.

def base(request):

    return render(request,'base.html')

def login(request):

    if request.method == 'POST':

        loginform = Loginform(request.POST)


        if loginform.is_valid():

            x = otp_send(request)



            return render(request, 'otpvalid.html')



    else:

        loginform=Loginform()

        return render(request, 'login.html', {'loginform': loginform})

def signup(request):

    if request.method=='POST':

        cust=signupform(request.POST)

        if cust.is_valid():

            cust.save()

        return render(request,'confirm.html')

    else:

        cust=signupform()



        return render(request,'signup.html',{'cust':cust})

def otpvalidation(request):

    newopt=request.POST["otp"]

    oldotp=request.session["otp"]

    if newopt==oldotp:



        return render(request,"home.html")

    else:

        return render(request,'otpvalid.html')



def otp_send(request):

    ot = str(random.randint(100000, 999999))

    # request.session["pwd"]=request.POST["t1"]



    temail=request.POST["email"]

    subject="registration otp"

    From_mail = settings.EMAIL_HOST_USER

    to_list = [temail]



    send_mail(subject, ot, From_mail, to_list, fail_silently=False)

    print("otp sent to email")

    request.session["details"] = request.POST

    request.session["otp"] = ot

def home(request):



    ser=request.GET['t1']

    fer=city.objects.filter(city=ser) or country.objects.filter(country=ser)

    return render(request,'home2.html',{'fer':fer})

class signuplist(APIView):

    def get(self,request,format=None):

        signups=signupserializer.objects.all()

        serializer=signupserializer(signups,many=True)

        return Response(serializer.data)

def logout(request):

    return render(request,'logout.html')