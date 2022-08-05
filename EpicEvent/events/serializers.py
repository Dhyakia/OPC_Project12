from rest_framework import serializers

from events.models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Client
        fields = ('id', 'contact_info', 'is_client', 'sales_contact')


class ContractSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Contract
        fields = ('id', 'amount', 'contract_status', 'client', 'sales_contact')


class EventSerializer(serializers.ModelSerializer):

    class Meta(object):
        modele = Event
        fields = ('id', 'notes', 'event_status', 'client', 'support_contact')