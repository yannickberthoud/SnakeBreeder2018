from django.contrib import admin
from .models import SlideShow, Album

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1

class SlideShowAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]

admin.site.register(SlideShow, SlideShowAdmin)