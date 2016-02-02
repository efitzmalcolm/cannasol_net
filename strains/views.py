from django.views import generic

from .models import Strain


class StrainListView(generic.ListView):
    model = Strain


class StrainDetailView(generic.DetailView):
    model = Strain
