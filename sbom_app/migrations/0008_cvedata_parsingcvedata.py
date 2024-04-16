# Generated by Django 4.2.5 on 2023-10-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbom_app', '0007_searchedata_delete_searche_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CveData',
            fields=[
                ('cve_id', models.CharField(db_column='CVE_ID', max_length=20, primary_key=True, serialize=False)),
                ('data', models.TextField(db_collation='utf8mb4_bin', db_column='DATA')),
            ],
            options={
                'db_table': 'CVE_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParsingCveData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve_id', models.CharField(blank=True, db_column='CVE_ID', max_length=20, null=True)),
                ('cpe23uri', models.CharField(blank=True, db_column='cpe23Uri', max_length=200, null=True)),
                ('versionstart', models.CharField(blank=True, db_column='versionStart', max_length=100, null=True)),
                ('versionend', models.CharField(blank=True, db_column='versionEnd', max_length=100, null=True)),
            ],
            options={
                'db_table': 'parsing_cve_data',
                'managed': False,
            },
        ),
    ]