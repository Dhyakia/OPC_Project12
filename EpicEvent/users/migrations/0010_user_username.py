# Generated by Django 3.2.14 on 2022-08-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='ANONYME', max_length=20, unique=True),
        ),
    ]
