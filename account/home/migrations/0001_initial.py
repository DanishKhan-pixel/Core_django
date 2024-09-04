# Generated by Django 5.1 on 2024-09-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_hire', models.DateField()),
            ],
        ),
    ]