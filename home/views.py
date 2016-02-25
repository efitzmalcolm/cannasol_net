from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import *
from .forms import RetailerContactForm


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
    context = {
        'page': AboutUsPage.objects.first(),
        'sections': AboutUsSection.objects.all(),
    }
    return render(request, 'home/about.html', context)


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


def retailerSignup(request):
    if request.method == 'GET':
        form = RetailerContactForm()
    else:
        form = RetailerContactForm(request.POST)
        if form.is_valid():
            newcontact = form.save()
            newcontact.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'home/retailer_signup.html', {
        'form': form,
        })
