from django.conf.urls import url

urlpatterns = [
    url(r'^about/', 'home.views.about', name='about'),
    url(r'^wheretobuy/', 'home.views.wheretobuy', name='wheretobuy'),
    url(r'^news/', 'home.views.news', name='news'),
    url(r'^$', 'home.views.index', name='home'),
]