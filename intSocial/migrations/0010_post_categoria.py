# Generated by Django 4.2.5 on 2023-12-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intSocial', '0009_alter_profile_imagen_alter_profile_imagen_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.CharField(default='Off-Topic', max_length=50, null=True),
        ),
    ]
