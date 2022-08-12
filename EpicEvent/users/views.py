from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from users.serializers import UserSerializer
from users.models import User


class UsersViewset(ModelViewSet):

    # All perm here are under: isAdminUser
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        user = self.request.user

        if user.is_superuser:
            query_users = User.objects.all()
            serializer_user = UserSerializer(query_users, many=True)
            return Response(serializer_user.data, status.HTTP_200_OK)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)


    def create(self, request):
        user = self.request.user

        if user.is_superuser:
            user = request.data
            serializer_user = UserSerializer(data=user)

            if serializer_user.is_valid(raise_exception=True):
                serializer_user.save()
                return Response(serializer_user.data, status.HTTP_201_CREATED)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def retrieve(self, request, pk=None):
        user = self.request.user

        if user.is_superuser:
            query_user = User.objects.get(id=pk)
            serializer_user = UserSerializer(query_user)
            return Response(serializer_user.data, status.HTTP_200_OK)

        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        user = self.request.user

        if user.is_superuser:
            if User.objects.filter(id=pk).exists():
                query_user = User.objects.filter(id=pk)
                new_role = request.data['role']

                a, b, c, d, = "0", "1", "2", "3"

                if new_role in {a, b, c, d}:
                    query_user.update(role=new_role)
                    serializer_user = UserSerializer(query_user, many=True)
                    return Response(serializer_user.data, status.HTTP_202_ACCEPTED)

                else:
                    message = "Role must be a number from 0 to 3"
                    return Response(message, status.HTTP_400_BAD_REQUEST)
        
            else:
                message = "Pas ou plus d'utilisateur à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)
    
    def destroy(self, request, pk=None):
        user = self.request.user

        if user.is_superuser:
            if User.objects.filter(id=pk).exists():
                query_user = User.objects.filter(id=pk)
                query_user.delete()
                message = "Utilisateur supprimé"
                return Response(message, status.HTTP_204_NO_CONTENT)         
        
            else:
                message = "Pas ou plus d'utilisateur à cette adresse"
                return Response(message, status.HTTP_404_NOT_FOUND)
        
        else:
            message = "Permission refusé"
            return Response(message, status.HTTP_403_FORBIDDEN)