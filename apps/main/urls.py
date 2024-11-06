from django.urls import path

from . import views


urlpatterns = [
    path('', views.AboutViewSet.as_view({'get': 'list',}), name='about-us'),
    path('contacts/', views.ContactsViewSet.as_view({'get': 'list', }), name='contacts'),
    path('address/', views.AddressViewSet.as_view({'get': 'list', }), name='about-us'),
]
