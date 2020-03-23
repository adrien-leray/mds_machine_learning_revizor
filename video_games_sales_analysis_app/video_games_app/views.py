from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    context={}
    return HttpResponse(render(context,"video_games_app/templates/index.html",request))