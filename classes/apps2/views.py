# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def next_page(request):
    return HttpResponse("<a href = '/apps1/index'> App1  </a>")
