from django.conf.urls import url

urlpatterns = [
    url(r'^about/', 'home.views.about', name='about'),
    url(r'^for_retailers/', 'home.views.retailerSignup', name='retailerSignup'),
    url(r'^wheretobuy/', 'home.views.wheretobuy', name='wheretobuy'),
    url(r'^news/', 'home.views.news', name='news'),
    url(r'^signup/', 'home.views.signup', name='signup'),
    url(r'^$', 'home.views.index', name='home'),
]
