# Generated by Django 2.1.5 on 2019-02-04 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autore',
            options={'verbose_name': 'Autore', 'verbose_name_plural': 'Autori'},
        ),
        migrations.AlterModelOptions(
            name='genere',
            options={'verbose_name': 'Genere', 'verbose_name_plural': 'Generi'},
        ),
        migrations.AlterModelOptions(
            name='libro',
            options={'verbose_name': 'Libro', 'verbose_name_plural': 'Libri'},
        ),
    ]