from django.contrib import admin
from strains.models import *


class TerpeneResultInline(admin.TabularInline):
    model = TerpeneResult
    extra = 0


class PotencyResultInline(admin.TabularInline):
    model = PotencyResult


class qaSampleAdmin(admin.ModelAdmin):

    # Feilds sets next!
    inlines = [
        PotencyResultInline,
        TerpeneResultInline,
    ]
    list_display = ('sample_id', 'lot_id', 'strain', 'sample_type', 'date_received')
    list_filter = ('strain', 'sample_type')
    search_fields = ['^sample_id', '^lot_id']
    show_full_result_count = True


class TerpeneResultAdmin(admin.ModelAdmin):

    pass


class PotencyResultAdmin(admin.ModelAdmin):
    pass


class StrainAdmin(admin.ModelAdmin):
    fields = ('name', 'desc', 'brand', 'preview_image', 'image')
    readonly_fields = ['preview_image']


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'desc', 'preview_image', 'logo')
    readonly_fields = ['preview_image']

admin.site.register(Strain, StrainAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(qaSample, qaSampleAdmin)
admin.site.register(Terpene)
admin.site.register(TerpeneResult, TerpeneResultAdmin)
admin.site.register(PotencyResult, PotencyResultAdmin)
