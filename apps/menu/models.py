from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', help_text='Дата и время создания записи')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления', help_text='Дата и время последнего обновления записи')

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Название категории', help_text='Введите название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']  # Сортировка по полю title по возрастанию

    def __str__(self):
        return self.title


class Tags(BaseModel):
    title = models.CharField(max_length=100, verbose_name='Название тега', help_text='Введите название тега (например, "Острое", "Вегетарианское")')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']  # Сортировка по полю title по возрастанию

    def __str__(self):
        return self.title


class Menu(BaseModel):
    image = models.ImageField(upload_to="images/", verbose_name='Изображение блюда', help_text='Загрузите изображение блюда')
    title = models.CharField(max_length=100, verbose_name='Название блюда', help_text='Введите название блюда')
    description = models.TextField(verbose_name='Описание блюда', help_text='Введите описание блюда')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items', verbose_name='Категория')
    tags = models.ManyToManyField(Tags, blank=True, related_name='menu_items', verbose_name='Теги')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', help_text='Введите цену блюда')
    is_active = models.BooleanField(default=True, verbose_name='Активно', help_text='Отметьте, если блюдо активно')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['title']  # Сортировка по полю title по возрастанию

    def __str__(self):
        return self.title


class Drink(BaseModel):
    image = models.ImageField(
        upload_to="images/drinks/",
        verbose_name="Изображение",
        help_text="Загрузите изображение напитка"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Введите название напитка"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание напитка"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберите категорию для напитка"
    )
    tags = models.ManyToManyField(
        Tags,
        verbose_name="Теги",
        help_text="Выберите теги для напитка"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        help_text="Введите цену напитка"
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Активный",
        help_text="Отметьте, если напиток активен"
    )

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'

    def __str__(self):
        return self.title