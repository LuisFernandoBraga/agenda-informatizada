# Generated by Django 5.1.2 on 2024-10-31 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0012_agenda_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sexo',
            new_name='Genero',
        ),
        migrations.AlterModelOptions(
            name='genero',
            options={'verbose_name': 'Gênero', 'verbose_name_plural': 'Gêneros'},
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='sexo',
            new_name='genero',
        ),
    ]
