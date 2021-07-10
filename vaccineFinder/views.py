from django.http import HttpResponse
from django.shortcuts import redirect,render

def basePage(request):
    return render(request, "base.html")