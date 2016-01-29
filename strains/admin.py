from django.contrib import admin
from cannasol_net.strains.models import *


admin.site.register(Strain, Brand, qaSample, Terpene)
