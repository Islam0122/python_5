from django.core.exceptions import ValidationError
from django.db import models


class About(models.Model):
    image = models.ImageField(upload_to='about_image',verbose_name="Изображение")
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок о нас')
    content = models.TextField(verbose_name='Контент', help_text='Введите текст о нас')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and About.objects.exists():
            raise ValidationError("Нельзя добавить более одного ")
        super().save(*args, **kwargs)


class Contacts(models.Model):
    phone = models.CharField(max_length=15, verbose_name='Телефон', help_text='Введите номер телефона')
    email = models.EmailField(verbose_name='Электронная почта', help_text='Введите электронную почту')
    whatsapp_url = models.URLField(verbose_name='URL WhatsApp', help_text='Введите URL для WhatsApp')
    telegram_url = models.URLField(verbose_name='URL Telegram', help_text='Введите URL для Telegram')
    instagram_url = models.URLField(verbose_name='URL Instagram', help_text='Введите URL для Instagram')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.phone

    def save(self, *args, **kwargs):
        if not self.pk and Contacts.objects.exists():
            raise ValidationError("Нельзя добавить более одного ")
        super().save(*args, **kwargs)


class Address(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок')
    address = models.CharField(max_length=150, verbose_name='Адрес', help_text='Введите адрес')
    map_location = models.URLField(verbose_name='Расположение на карте',
                                   help_text='Введите URL для отображения на карте')
    working_hours = models.CharField(max_length=100, verbose_name='Рабочие часы', help_text='Введите рабочие часы')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if Address.objects.count() > 1:
            super().delete(*args, **kwargs)
        else:
            raise ValidationError("Нельзя удалить последний адрес")
