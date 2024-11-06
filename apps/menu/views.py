from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagsViewSet(ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class MenuViewSet(ModelViewSet):
    queryset = Menu.objects.filter(is_active=True)
    serializer_class = MenuSerializer


class DrinkViewSet(ModelViewSet):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.filter(is_active=True)

