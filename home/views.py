from django.shortcuts import render

# Create your views here.


def index(request):
    """ Rendering index view """

    return render(request, 'home/index.html')
