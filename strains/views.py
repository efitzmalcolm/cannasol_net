from django.views.generic.list import ListView

from .models import Strain


class StrainListView(ListView):
    model = Strain
