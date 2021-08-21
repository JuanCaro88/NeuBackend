# Generated by Django 3.2.6 on 2021-08-21 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrie',
            options={'ordering': ['name_countrie', 'city', 'state', 'population'], 'verbose_name': 'Countrie', 'verbose_name_plural': 'Countries'},
        ),
        migrations.RenameField(
            model_name='countrie',
            old_name='cities',
            new_name='city',
        ),
        migrations.AlterUniqueTogether(
            name='countrie',
            unique_together={('name_countrie', 'city', 'state', 'population')},
        ),
    ]