# Generated by Django 3.0.14 on 2022-09-22 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='FechaCompra',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='estadoLectura',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='numeroLeidas',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='libro',
            name='numeroPaginas',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
