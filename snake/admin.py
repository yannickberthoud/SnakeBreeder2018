from django.contrib import admin
from .models import Family, Venom, Snake, Album, SearchingSnake, SalingSnake, AlbumForSale

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
        ('Détention', {'fields': ['old', 'newborn']})
    ]
    list_display = ('family', 'scientific_name')
    list_filter = ['family']
    search_fields = ['scientific_name']
    inlines = [AlbumInline]

    prepopulated_fields = {"slug": ("scientific_name",)}

admin.site.register(Snake, SnakeAdmin)

class AlbumForSaleInline(admin.TabularInline):
    model = AlbumForSale
    extra = 1

class SalingSnakeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['family', 'scientific_name', 'slug', 'disponibilities', 'comments']}),
        ('Toxicologie', {'fields': ['venom']}),
        ('Contrôle', {'fields': ['subject']}),
        ('Tarification', {'fields': ['price', 'price_couple']})
    ]
    list_display = ('family', 'scientific_name')
    list_filter = ['family']
    search_fields = ['scientific_name']
    inlines = [AlbumForSaleInline]

    prepopulated_fields = {"slug": ("scientific_name",)}

admin.site.register(SalingSnake, SalingSnakeAdmin)

class SearchingSnakeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['species_list']}),
    ]

    list_display = ('species_list',)

admin.site.register(SearchingSnake, SearchingSnakeAdmin)
