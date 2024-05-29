from django.contrib import admin
from .models import Region, District, School, Sinf

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name',)
    list_filter = ('region',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'district')
    search_fields = ('name',)
    list_filter = ('district',)

class SinfAdmin(admin.ModelAdmin):
    list_display = ('name', 'school')
    search_fields = ('name',)
    list_filter = ('school',)

admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Sinf, SinfAdmin)
