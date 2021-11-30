from django.shortcuts import render

# Create your views here.

def guest_home(request):
    return render(request, 'tracker/guest.html')