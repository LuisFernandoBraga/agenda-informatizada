# Generated by Django 5.1.2 on 2024-10-21 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_faixa_etaria_agenda_faixa_etaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]