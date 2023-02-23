# Generated by Django 4.1.5 on 2023-02-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0008_remove_pedalclon_precio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventapropio',
            name='precio',
        ),
        migrations.AddField(
            model_name='pedalclon',
            name='fechapedido',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='pedalreparar',
            name='fechapedido',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='ventapropio',
            name='fechapedido',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='pedalreparar',
            name='envio',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='ventapropio',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
