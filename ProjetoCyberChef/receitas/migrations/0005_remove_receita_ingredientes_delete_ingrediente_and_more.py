# Generated by Django 4.2.7 on 2023-11-23 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0004_ingrediente_remove_receita_ingredientes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='ingredientes',
        ),
        migrations.DeleteModel(
            name='Ingrediente',
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
