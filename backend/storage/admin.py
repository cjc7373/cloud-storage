from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin

from .models import MyFile, Catalogue

# Register your models here.

@admin.register(MyFile)
class MyFile(admin.ModelAdmin):
    list_display = (
        'res_path',
        'size',
        'date_joined',
        'reference_count',
        'is_legal'
    )

@admin.register(Catalogue)
class Catalogue(DraggableMPTTAdmin):
    pass