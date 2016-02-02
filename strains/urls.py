from django.conf.urls import url

from .views import StrainListView

urlpatterns = [
    url(r'^strains/', StrainListView.as_view(), name='strain-list'),
]
