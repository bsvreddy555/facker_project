from django.shortcuts import render
from django.http.response import HttpResponse
from faker import Faker
from .models import student

fack=Faker()

# Create your views here.

def student_fack(request):
    for i in range(100):
        name=fack.name()
        email=fack.email()
        salary=fack.random_element(elements=(1000,2000,3000))
        job=fack.random_element(elements=('HR','Manager','Team Leader'))
        location=fack.random_element(elements=('HYD','BLNR','CHENNAI'))

        data=student(
            name=name,
            email=email,
            salary=salary,
            job=job,
            location=location
        )
        data.save()
    return HttpResponse('data save successfully ')

