# Generated by Django 3.2.12 on 2023-02-24 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ClassView', '0004_rename_username_register_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Password',
            new_name='password',
        ),
    ]
