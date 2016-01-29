from django.shortcuts import render_to_response


def index(request):
    return render_to_response('home/index.html')

def about(request):
    return render_to_response('home/about.html')

def strains(request):
    return render_to_response('home/strains.html')

def wheretobuy(request):
    return render_to_response('home/wheretobuy.html')

def news(request):
    return render_to_response('home/news.html')