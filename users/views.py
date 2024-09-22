# from django.contrib.admin.options import HttpResponseRedirect
# from django.contrib.admin.widgets import reverse
from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, "login.html")
