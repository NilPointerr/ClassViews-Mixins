# Generated by Django 3.2.12 on 2023-02-24 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClassView', '0003_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Username',
            new_name='username',
        ),
    ]
