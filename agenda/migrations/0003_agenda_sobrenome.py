# Generated by Django 5.1.2 on 2024-10-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_rename_created_date_agenda_data_hora_agenda_valor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
