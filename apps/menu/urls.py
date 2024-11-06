from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('category/', views.CategoryViewSet.as_view({'get': 'list',}), name='category'),
    path('tags/', views.TagsViewSet.as_view({'get': 'list', }), name="tags"),
    path('menu/', views.MenuViewSet.as_view({'get': 'list', }), name='menu'),
    path('menu/<int:pk>/', views.MenuViewSet.as_view({'get': 'retrieve'})),
    path('drink/', views.DrinkViewSet.as_view({'get': 'list', }), name='drink'),
    path('drink/<int:pk>/', views.DrinkViewSet.as_view({'get': 'retrieve'})),
]