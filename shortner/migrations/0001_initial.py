# Generated by Django 4.2.1 on 2023-05-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=1000)),
                ('short_url', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
