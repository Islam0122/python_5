from django.contrib import admin
from django.utils.html import format_html

from .models import About, Contacts, Address


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'phone', 'email',
        'whatsapp_link', 'telegram_link',
        'instagram_link',
    )

    fieldsets = (
        (None, {
            'fields': ('phone', 'email')
        }),
        ('WhatsApp', {
            'fields': ('whatsapp_url',)
        }),
        ('Telegram', {
            'fields': ('telegram_url',)
        }),
        ('Instagram', {
            'fields': ('instagram_url',)
        }),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return Contacts.objects.exists()

    # Метод для кликабельной ссылки на WhatsApp
    def whatsapp_link(self, obj):
        return format_html('<a href="{}" target="_blank">WhatsApp</a>', obj.whatsapp_url)
    whatsapp_link.short_description = 'WhatsApp'

    # Метод для кликабельной ссылки на Telegram
    def telegram_link(self, obj):
        return format_html('<a href="{}" target="_blank">Telegram</a>', obj.telegram_url)
    telegram_link.short_description = 'Telegram'

    # Метод для кликабельной ссылки на Instagram
    def instagram_link(self, obj):
        return format_html('<a href="{}" target="_blank">Instagram</a>', obj.instagram_url)
    instagram_link.short_description = 'Instagram'


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'working_hours')
    fieldsets = (
        (None, {
            'fields': ('title', 'address')
        }),
        ('Расположение', {
            'fields': ('map_location',)
        }),
        ('Рабочие часы', {
            'fields': ('working_hours',)
        }),
    )

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None:
            return Address.objects.count() > 1
        return True

    def has_change_permission(self, request, obj=None):
        return Address.objects.exists()


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

    fieldsets = (
        (None, {
            'fields': ('display_image','image', 'title', 'content')
        }),
    )
    readonly_fields =( "display_image",)

    # Метод для отображения изображения
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100%" height="100%" />'.format(obj.image.url))
        return "Нет изображения"
    display_image.short_description = 'Изображение'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return About.objects.exists()

