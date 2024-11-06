from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title',)


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title','category','price','created_at','is_active')
    readonly_fields = ('created_at', 'updated_at','display_image',)
    search_fields = ('title','price',)
    list_filter = ('category','tags', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('display_image', 'image', 'title','description', 'category', 'tags', 'price', 'created_at', 'updated_at','is_active')
        }),
    )

    # Метод для отображения изображения
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.image.url))
        return "Нет изображения"

    display_image.short_description = 'Изображение'


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'display_image',)
    search_fields = ('title', 'description',)
    list_filter = ('category', 'tags', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('display_image', 'image', 'title', 'description', 'category', 'tags', 'price', 'is_active')
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.image.url))
        return "Нет изображения"

    display_image.short_description = 'Изображение'


