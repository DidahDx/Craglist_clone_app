from django.shortcuts import render


# Create your views here.
# Are used to return the webpages
def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')
    send_to_frontend = {
        'search': search,
    }
    return render(request, 'my_app/new_search.html',send_to_frontend)
