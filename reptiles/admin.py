from django.contrib import admin

from reptiles.models import Repartition, Environment

class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Environment, EnvironmentAdmin)

class RepartitionAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Repartition, RepartitionAdmin)













