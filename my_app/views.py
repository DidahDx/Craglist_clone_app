from django.shortcuts import render


# Create your views here.
# Are used to return the webpages
def home(request):
    return render(request, 'base.html')
