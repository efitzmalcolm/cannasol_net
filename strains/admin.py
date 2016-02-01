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
    list_display = ('qa_sample', 'terpene', 'result', 'get_strain')
    list_filter = ('terpene', 'qa_sample__strain')
    list_display_links = ['result']
    search_fields = ['^qa_sample']
    show_full_result_count = True

    def get_strain(self, obj):
        return obj.qa_sample.strain
    get_strain.short_description = 'Strain'
    get_strain.admin_order_field = 'qa_sample__strain'


class PotencyResultAdmin(admin.ModelAdmin):
    pass


class StrainAdmin(admin.ModelAdmin):
    fields = (('name', 'brand'), 'desc', 'preview_image', 'image')
    readonly_fields = ['preview_image']
    list_display = ('name', 'brand')
    list_filter = ['brand']
    search_fields = ['^name']
    ordering = ['name']


class BrandAdmin(admin.ModelAdmin):
    fields = ('name', 'desc', 'preview_image', 'logo')
    readonly_fields = ['preview_image']


admin.site.register(Strain, StrainAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(qaSample, qaSampleAdmin)
admin.site.register(Terpene)
admin.site.register(TerpeneResult, TerpeneResultAdmin)
admin.site.register(PotencyResult, PotencyResultAdmin)
