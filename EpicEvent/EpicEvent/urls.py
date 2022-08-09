from multiprocessing.connection import Client
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.views import UsersViewset
from events.views import ClientsViewset, ContractsViewset, EventsViewset


router = routers.SimpleRouter()
router.register(r'users', UsersViewset)
router.register(r'clients' ,ClientsViewset)
router.register(r'contracts', ContractsViewset)
router.register(r'events', EventsViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
