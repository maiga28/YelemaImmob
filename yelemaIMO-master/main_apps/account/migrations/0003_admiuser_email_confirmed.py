# Generated by Django 4.2.6 on 2023-11-28 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_admiuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='admiuser',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]