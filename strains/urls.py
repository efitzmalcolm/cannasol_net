from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^strains/$', views.StrainListView.as_view(), name='strain-list'),
    url(r'^strains/(?P<pk>[0-9]+)/$', views.StrainDetailView.as_view(), name='strain-detail'),
]
