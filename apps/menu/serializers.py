from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagsSerializer(many=True)  # Обратите внимание на использование many=True

    class Meta:
        model = Menu
        fields = ('id', 'title', 'description', 'category', 'tags', 'price', 'is_active')

    def create(self, validated_data):
        # Извлекаем данные для категории и тегов
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')

        # Создаём категорию
        category = Category.objects.create(**category_data)

        # Создаём меню
        menu_item = Menu.objects.create(category=category, **validated_data)

        # Создаём и добавляем теги
        for tag_data in tags_data:
            tag, created = Tags.objects.get_or_create(**tag_data)
            menu_item.tags.add(tag)

        return menu_item

    def update(self, instance, validated_data):
        # Обновляем категорию
        category_data = validated_data.pop('category', None)
        if category_data:
            for attr, value in category_data.items():
                setattr(instance.category, attr, value)
            instance.category.save()

        # Обновляем теги
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, created = Tags.objects.get_or_create(**tag_data)
                instance.tags.add(tag)

        # Обновляем остальные поля
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class DrinkSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagsSerializer(many=True)

    class Meta:
        model = Drink
        fields = '__all__'