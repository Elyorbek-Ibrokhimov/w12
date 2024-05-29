from django.contrib import admin
from .models import Region, District

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name',)
    list_filter = ('region',)

admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)