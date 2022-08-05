from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from events.models import Client, Contract, Event
from events.serializers import ClientSerializer, ContractSerializer, EventSerializer


class ClientViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    dataset = Client.objects.all()

    # TODO: write the calls


class ContractViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = ContractSerializer
    dataset = Contract.objects.all()

    # TODO: write the calls


class EventViewset(ModelViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    dataset = Event.objects.all()

    # TODO: write the calls