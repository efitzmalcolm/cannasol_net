from django.contrib import admin
from strains.models import *


class TerpeneResultInline(admin.TabularInline):
    model = TerpeneResult


class PotencyResultInline(admin.TabularInline):
    model = PotencyResult

class qaSampleAdmin(admin.ModelAdmin):
    inlines = [
        TerpeneResultInline,
        PotencyResultInline
    ]
    list_display = ('date_received', 'strain', 'sample_type', 'sample_id', 'lot_id')
    list_filter = ('strain', 'sample_type')
    search_fields = ['^sample_id', '^lot_id']
    show_full_result_count = True


class TerpeneResultAdmin(admin.ModelAdmin):

    pass


class PotencyResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Strain)
admin.site.register(Brand)
admin.site.register(qaSample, qaSampleAdmin)
admin.site.register(Terpene)
admin.site.register(TerpeneResult, TerpeneResultAdmin)
admin.site.register(PotencyResult, PotencyResultAdmin)
