from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    context = {'latest_question_list': "null"}

    return HttpResponse(render(request,"video_games_app/index.html",context))