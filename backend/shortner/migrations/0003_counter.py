# Generated by Django 4.2.9 on 2024-02-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0002_rename_shortner_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
            ],
        ),
    ]