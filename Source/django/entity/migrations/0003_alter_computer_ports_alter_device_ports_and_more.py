# Generated by Django 5.1.3 on 2024-12-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_license_licensesession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='ports',
            field=models.ManyToManyField(blank=True, null=True, to='entity.port', verbose_name='Portlar'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ports',
            field=models.ManyToManyField(blank=True, null=True, to='entity.port', verbose_name='Portlar'),
        ),
        migrations.AlterField(
            model_name='monitor',
            name='ports',
            field=models.ManyToManyField(blank=True, null=True, to='entity.port', verbose_name='Portlar'),
        ),
        migrations.AlterField(
            model_name='network',
            name='ports',
            field=models.ManyToManyField(blank=True, null=True, to='entity.port', verbose_name='Portlar'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='ports',
            field=models.ManyToManyField(blank=True, null=True, to='entity.port', verbose_name='Portlar'),
        ),
    ]
