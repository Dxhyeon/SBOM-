# Generated by Django 4.2.5 on 2023-10-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbom_app', '0003_searche_data_alter_sbom_data_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searche_data',
            name='id',
            field=models.BigIntegerField(primary_key='False', serialize=False),
        ),
    ]