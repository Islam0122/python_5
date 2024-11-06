from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import About, Address, Contacts
from .serializers import AboutSerializer, ContactsSerializer, AddressSerializer


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

