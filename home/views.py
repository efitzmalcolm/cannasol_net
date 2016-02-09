from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from .models import *


def index(request):

    context = {
        'carousel_images': CarouselImage.objects.all(),
        'brand_section': BrandSection.objects.first(),
        'brand_items': BrandItem.objects.all(),
        'info_section': InfoSection.objects.first(),
        'team_members': TeamMember.objects.all(),
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def wheretobuy(request):
    context = {'retailers': Retailer.objects.all()}
    return render(request, 'home/wheretobuy.html', context)


def news(request):
    return render(request, 'home/news.html')


def signup(request):
    try:
        NewsletterContact.objects.create(email=request.POST['EMAIL'])
    except:
        pass

    return HttpResponseRedirect(request.GET['next'])
