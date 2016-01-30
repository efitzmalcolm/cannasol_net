from django.contrib import admin
from strains.models import *


class TerpeneResultInline(admin.TabularInline):
    model = TerpeneResult


class qaSampleAdmin(admin.ModelAdmin):
    inlines = [
        TerpeneResultInline,
    ]


class TerpeneResultAdmin(admin.ModelAdmin):

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Strain)
admin.site.register(Brand)
admin.site.register(qaSample, qaSampleAdmin)
admin.site.register(Terpene)
admin.site.register(TerpeneResult)
