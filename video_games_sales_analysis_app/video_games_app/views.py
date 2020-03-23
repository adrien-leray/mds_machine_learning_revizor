from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request,"video_games_app/index.html",{}))

def pie_chart(request):
    labels = []
    data = []
    labels.append("yo1")
    labels.append("yo2")
    labels.append("yo3")
    labels.append("yo4")
    labels.append("yo5")

    data.append("15")
    data.append("15")
    data.append("26")
    data.append("35")
    data.append("5")

    return HttpResponse(render(request, 'video_games_app/pie_chart.html', {
            'labels': labels,
            'data': data,
    }))