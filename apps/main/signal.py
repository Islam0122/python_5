from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import About, Contacts, Address

text = ('Добро пожаловать в наш магазин diskg_one01_store! Мы предлагаем широкий ассортимент одежды и обуви для всей '
        'семьи. '
        'У нас вы найдете как повседневную, так и стильную одежду, обувь на любой вкус и сезон. Мы стремимся '
        'предоставить нашим '
        'клиентам высококачественные товары по доступным ценам и гарантируем отличный сервис. Будьте уверены, '
        'что каждая покупка '
        'будет удовлетворять ваши ожидания. Благодарим вас за выбор нашего магазина!')


@receiver(post_migrate)
def create_about_us(sender, **kwargs):
    if About.objects.count() == 0:
        About.objects.create(
            image='./img.png',
            title='О нас',
            content=text,
        )
    if Contacts.objects.count() == 0:
        Contacts.objects.create(
            phone='+1234567890',
            email='contact@example.com',
            whatsapp_url='https://wa.me/1234567890',
            telegram_url='https://t.me/username',
            instagram_url='https://instagram.com/username',
        )

    if Address.objects.count() == 0:
        Address.objects.create(
            title='Главный офис',
            address='1234 Main St, Springfield, USA',
            map_location='https://maps.example.com/?q=1234+Main+St,+Springfield,+USA',
            working_hours='Пн-Пт: 9:00 - 18:00'
        )