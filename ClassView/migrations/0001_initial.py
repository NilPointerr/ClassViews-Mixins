# Generated by Django 3.2.12 on 2023-02-10 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
