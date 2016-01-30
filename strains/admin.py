from django.contrib import admin
from strains.models import *


class TerpeneResultInline(admin.TabularInline):
    model = TerpeneResult


class qaSampleAdmin(admin.ModelAdmin):
    inlines = [
        TerpeneResultInline,
    ]


admin.site.register(Strain)
admin.site.register(Brand)
admin.site.register(qaSample, qaSampleAdmin)
admin.site.register(Terpene)
admin.site.register(TerpeneResult)
