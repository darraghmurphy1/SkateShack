from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to display index page """

    return render(request, 'home/index.html')


def error(request):
    """ A view to display index page """

    template: 'home/404.html'

    return render(request, template)