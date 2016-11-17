"""
Author: Thaiseer Parammal
"""

from django.template import loader
from django.http import HttpResponse
from . import function


def home(request):
    template = loader.get_template('earthquake/index.html')
    return HttpResponse(template.render({}, request))


def index(request):
    context = {'title': function.gettitle(), 'time': function.gettime(), 'latlong': function.getlatlong(),
               'link': function.getlink()}
    template = loader.get_template('earthquake/earthquake.html')
    return HttpResponse(template.render(context, request))


def landslide(request):
    context = {'title': function.gettitle(), 'time': function.gettime(), 'latlong': function.getlatlong(),
               'link': function.getlink()}
    template = loader.get_template('earthquake/landslide.html')
    return HttpResponse(template.render(context, request))


def forest_fire(request):
    context = {'title': function.gettitle(), 'time': function.gettime(), 'latlong': function.getlatlong(),
               'link': function.getlink()}
    template = loader.get_template('earthquake/forest_fire.html')
    return HttpResponse(template.render(context, request))
