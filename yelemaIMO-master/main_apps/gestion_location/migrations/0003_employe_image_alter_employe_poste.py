# Generated by Django 4.2.6 on 2023-11-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_location', '0002_employe_user_auth_alter_employe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='image',
            field=models.ImageField(default=2, upload_to='image/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employe',
            name='poste',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]