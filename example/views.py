from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sleepy, send_email_task

def index(request):
    send_email_task()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT!</h1>')
