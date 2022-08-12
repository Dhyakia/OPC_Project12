from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from events.models import Client, Contract, Event
from events.serializers import ClientSerializer, ContractSerializer, EventSerializer


SELLER = "1"
SUPPORT = "2"

class ClientsViewset(ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    
    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['is_client']
    search_fields = ['id', 'contact_info', 'is_client']
    ordering_fields = ['id']
    ordering = ['id']

    def list(self, request):
        # perm: admin / seller / support
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset()).filter()

        if user.is_superuser or user.role == SELLER or user.role == SUPPORT:
            serializer_client = self.serializer_class(queryset, many=True)
            return Response(serializer_client.data, status.HTTP_200_OK)
        
        message = "Permission refusé"
        return Response(message, status.HTTP_403_FORBIDDEN)

    def create(self, request):
        # perm: admin / seller
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            client = request.data
            serializer_client = self.serializer_class(data=client)

            if serializer_client.is_valid(raise_exception=True):
                serializer_client.save()
                return Response(serializer_client.data, status.HTTP_201_CREATED)
        
        message = "Permission refusé"
        return Response(message, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        # perm: admin / seller (sales_contact=current_user)
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            if user.role == SELLER:
                if Client.objects.filter(id=pk, sales_contact=user.id).exists():
                    pass
                else:
                    message = "Ce client ne vous ais pas attribué"
                    return Response(message, status.HTTP_403_FORBIDDEN)

            query_client = Client.objects.get(id=pk)
            serializer_client = self.serializer_class(query_client)
            return Response(serializer_client.data, status.HTTP_200_OK)                

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        # perm: admin / seller (sales_contact=current_user)
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            if user.role == SELLER:
                if Client.objects.filter(id=pk, sales_contact=user.id).exists():
                    pass
                else:
                    message = "Ce client ne vous ais pas attribué"
                    return Response(message, status.HTTP_403_FORBIDDEN)

            if Client.objects.filter(id=pk).exists():
                query_client = Client.objects.filter(id=pk)
                new_contact_info = request.data['contact_info']
                new_is_client = request.data['is_client']
                new_sales_contact = request.data['sales_contact']

                query_client.update(
                    contact_info=new_contact_info,
                    is_client=new_is_client,
                    sales_contact=new_sales_contact
                )
                serializer_client = self.serializer_class(query_client, many=True)
                return Response(serializer_client.data, status.HTTP_202_ACCEPTED)

            else:
                message = "Pas ou plus d'utilisateur à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # perm: admin
        user = self.request.user

        if user.is_superuser:
            if Client.objects.filter(id=pk).exists():
                query_client = Client.objects.filter(id=pk)
                query_client.delete()
                message = "Client supprimé"
                return Response(message, status.HTTP_204_NO_CONTENT)

            else:
                message = "Pas ou plus de client à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)


class ContractsViewset(ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated]

    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['amount']
    search_fields = ['id', 'contract_status']
    ordering_fields = ['id']
    ordering = ['id']


    def list(self, request):
        # perm: admin / seller
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset()).filter()

        if user.is_superuser or user.role == SELLER:
            seriallizer_contract = ContractSerializer(queryset, many=True)
            return Response(seriallizer_contract.data, status.HTTP_200_OK)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def create(self, request):
        # perm: admin / seller
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            contract = request.data
            serializer_contract = ContractSerializer(data=contract)

            if serializer_contract.is_valid(raise_exception=True):
                serializer_contract.save()
                return Response(serializer_contract.data, status.HTTP_201_CREATED)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        # perm: admin / seller (sales_contact=current_user)
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            if user.role == SELLER:
                if Contract.objects.filter(id=pk, sales_contact=user.id).exists():
                    pass
                else:
                    message = "Ce contrat ne vous ais pas attribué"
                    return Response(message, status.HTTP_403_FORBIDDEN)

            query_contract = Contract.objects.get(id=pk)
            serializer_contract = ContractSerializer(query_contract)
            return Response(serializer_contract.data, status.HTTP_200_OK)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        # perm: admin / seller (sales_contact=current_user)
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            if user.role == SELLER:
                if Contract.objects.filter(id=pk, sales_contact=user.id).exists():
                    pass
                else:
                    message = "Ce contrat ne vous ais pas attribué"
                    return Response(message, status.HTTP_403_FORBIDDEN)

            if Contract.objects.filter(id=pk).exists():
                query_contract = Contract.objects.filter(id=pk)
                new_amount = request.data["amount"]
                new_contract_status = request.data["contract_status"]
                new_sales_contact = request.data["sales_contact"]

                query_contract.update(
                    amount=new_amount,
                    contract_status=new_contract_status,
                    sales_contact=new_sales_contact
                )
                serializer_contract = ContractSerializer(query_contract, many=True)
                return Response(serializer_contract.data, status.HTTP_202_ACCEPTED)

            else:
                message = "Pas ou plus d'utilisateur à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # perm: admin
        user = self.request.user

        if user.is_superuser:
            if Contract.objects.filter(id=pk).exists():
                query_contract = Contract.objects.filter(id=pk)
                query_contract.delete()
                message = "Contrat supprimé"
                return Response(message, status.HTTP_204_NO_CONTENT)

            else:
                message = "Pas ou plus de contrat à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)
            
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)


class EventsViewset(ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]    

    # Filters
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['event_status']
    search_fields = ['id', 'notes']
    ordering_fields = ['id']
    ordering = ['id']


    def list(self, request):
        # perm: admin / seller / support
        user = self.request.user
        queryset = self.filter_queryset(self.get_queryset()).filter()

        if user.is_superuser or user.role == SELLER or user.role == SUPPORT:
            serializer_event = EventSerializer(queryset, many=True)
            return Response(serializer_event.data, status.HTTP_200_OK)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def create(self, request):
        # perm: admin / seller
        user = self.request.user

        if user.is_superuser or user.role == SELLER:
            event = request.data
            serializer_event = EventSerializer(data=event)

            if serializer_event.is_valid(raise_exception=True):
                serializer_event.save()
                return Response(serializer_event.data, status.HTTP_201_CREATED)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        # perm: admin / support (support_contact=current_user)
        user = self.request.user

        if user.is_superuser or user.role == SUPPORT:
            if user.role == SUPPORT:
                if Event.objects.filter(id=pk, support_contact=user.id).exists():
                    pass
                else:
                    message = "Cet evenement ne vous ais pas attribué"
                    return Response(message, status.HTTP_403_FORBIDDEN)

            query_event = Event.objects.get(id=pk)
            serializer_event = EventSerializer(query_event)
            return Response(serializer_event.data, status.HTTP_200_OK)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        # perm: admin / support (support_contact=current_user)
        user = self.request.user

        if user.is_superuser or user.role == SUPPORT:
            if user.role == SUPPORT:
                if Event.objects.filter(id=pk, support_contact=user.id).exists():
                    pass
                else:
                    message = "Cet evenement ne vous ais pas attribué"
                    return Response(message, status.HTTP_403_FORBIDDEN)

            if Event.objects.filter(id=pk).exists():
                query_event = Event.objects.filter(id=pk)
                new_notes = request.data['notes']
                new_event_status = request.data['event_status']
                new_support_contact = request.data['support_contact']


                query_event.update(
                    notes=new_notes,
                    event_status=new_event_status,
                    support_contact=new_support_contact
                )
                serializer_event = EventSerializer(query_event, many=True)
                return Response(serializer_event.data, status.HTTP_202_ACCEPTED)
            
            else:
                message = "Pas ou plus d'utilisateur à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        # perm: admin
        user = self.request.user

        if user.is_superuser:
            if Event.objects.filter(id=pk).exists():
                query_event = Event.objects.filter(id=pk)
                query_event.delete()
                message = "Evenement supprimé"
                return Response(message, status.HTTP_204_NO_CONTENT)         
        
            else:
                message = "Pas ou plus d'évenement à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)
