from django.contrib import admin
from lizard.models import Lizard, Album

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1

class LizardAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("scientific_name",)}
    inlines = [AlbumInline]

admin.site.register(Lizard, LizardAdmin)