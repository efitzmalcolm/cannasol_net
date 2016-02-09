from django.contrib import admin
from home.models import *


class CarouselAdmin(admin.ModelAdmin):
    fields = ('name', 'header', 'preview_image', 'image')
    readonly_fields = ['preview_image']


class BrandItemInline(admin.TabularInline):
    model = BrandItem
    extra = 0
    fields = ('name', 'desc', 'preview_image', 'image')
    readonly_fields = ['preview_image']


class BrandSectionAdmin(admin.ModelAdmin):
    fields = ('title', 'intro')

    inlines = [BrandItemInline]

    def has_add_permission(self, request):
        base_add_permission = super(BrandSectionAdmin, self).has_add_permission(request)
        if base_add_permission:
            return not BrandSection.objects.exists()


class InfoSectionAdmin(admin.ModelAdmin):
    fields = ('text', 'preview_image', 'image')
    readonly_fields = ['preview_image']

    def has_add_permission(self, request):
        base_add_permission = super(InfoSectionAdmin, self).has_add_permission(request)
        if base_add_permission:
            return not InfoSection.objects.exists()


class TeamMemberAdmin(admin.ModelAdmin):
    fields = ('name', 'bio', 'email', 'preview_image', 'image')
    readonly_fields = ['preview_image']


class RetailerAdmin(admin.ModelAdmin):
    fields = ('name', 'preview_image', 'image')
    readonly_fields = ['preview_image']


admin.site.register(CarouselImage, CarouselAdmin)
admin.site.register(BrandSection, BrandSectionAdmin)
admin.site.register(InfoSection, InfoSectionAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Retailer, RetailerAdmin)
