from django.db import models

from users.models import User


class Client(models.Model):

    contact_info = models.CharField(max_length=200)
    is_client = models.BooleanField(default=False)

    sales_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    

class Contract(models.Model):

    amount = models.IntegerField()
    contract_status = models.BooleanField(default=False)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sales_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


class Event(models.Model):

    notes = models.CharField(max_length=2000)
    event_status = models.BooleanField(default=False)

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    support_contact = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)