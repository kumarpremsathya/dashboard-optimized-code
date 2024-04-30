# Generated by Django 4.2.9 on 2024-04-23 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probe_agile_data', '0009_mca_log_remove_sebi_log_data_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='irdai_log',
            fields=[
                ('Sr_no', models.AutoField(primary_key=True, serialize=False)),
                ('source_name', models.CharField(max_length=255)),
                ('script_status', models.CharField(max_length=255)),
                ('data_available', models.IntegerField(default=0)),
                ('data_scraped', models.IntegerField(default=0)),
                ('total_record_count', models.IntegerField(default=0)),
                ('failure_reason', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('source_status', models.CharField(default='Active', max_length=255)),
                ('date_of_scraping', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'irdai_log',
            },
        ),
    ]