from django.contrib import admin
from .models import Family, Venom, Snake, Album

class FamilyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    ordering = ['name']
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Family, FamilyAdmin)

class VenomAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Venom, VenomAdmin)

class AlbumInline(admin.TabularInline):
    model = Album
    extra = 1

class SnakeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['family', 'scientific_name', 'slug', 'sex', 'description']}),
        ('Toxicologie', {'fields': ['venom', 'dentition']}),
        ('Moeurs & Biotope', {'fields': ['moeurs', 'life', 'environment', 'repartition', 'reproduction']}),
        ('Achat & ventes', {'fields': ['business', 'price', 'price_couple']}),
        ('Détention', {'fields': ['old']})
    ]
    list_display = ('family', 'scientific_name', 'business', 'price', 'price_couple')
    list_filter = ['family', 'business']
    search_fields = ['scientific_name']
    inlines = [AlbumInline]

    prepopulated_fields = {"slug": ("scientific_name",)}

admin.site.register(Snake, SnakeAdmin)