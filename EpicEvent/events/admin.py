from django.contrib import admin

from events.models import Client, Contract, Event


class ClientAdmin(admin.ModelAdmin):
    list_display = ('contact_info', 'is_client', 'sales_contact')

class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_status', 'amount', 'client', 'sales_contact')

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_status', 'notes', 'client', 'support_contact')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Event, EventAdmin)