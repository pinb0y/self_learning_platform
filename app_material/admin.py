from django.contrib import admin

from app_material.models import Section, Material, Subscription


class SectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class MaterialAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Section, SectionAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Subscription)
