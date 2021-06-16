from django.contrib import admin
from .models import Category, Ecv

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Ecv)
class EcvAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}


