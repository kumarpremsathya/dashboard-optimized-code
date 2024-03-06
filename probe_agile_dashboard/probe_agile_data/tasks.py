from celery import shared_task, task
from celery import periodic_task
from celery.decorators import periodic_task
from django.utils import timezone
from datetime import timedelta
from .models import rbi_log
import configparser
import os

from django.db.models import F
from django.db import models



def get_status_from_config(source_name):
    config_path = get_config_path(source_name)
    config = configparser.ConfigParser()
    config.read(config_path)
    return config.get(source_name, 'status')

def get_config_path(source_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_folder = os.path.join(base_dir, 'config')
    config_file = f'config_{source_name.lower()}.ini'
    return os.path.join(config_folder, config_file)


# Function to get a unique Sr_no value
def get_unique_sr_no():
    max_sr_no = rbi_log.objects.using('rbi').aggregate(models.Max('Sr_no'))['Sr_no__max']
    return max_sr_no + 1 if max_sr_no is not None else 1


@periodic_task(run_every=timedelta(seconds=1))  # Adjust the frequency as needed
def update_database_periodic_task():
    # Update the corresponding status in the database here
    # Example:
    update_database('rbi_fema', get_status_from_config('rbi_fema'))
    update_database('rbi_ecb', get_status_from_config('rbi_ecb'))
    update_database('rbi_odi', get_status_from_config('rbi_odi'))
    update_database('startupindia', get_status_from_config('startupindia'))

@shared_task
def update_database_task(source_name, status):
    # Update the corresponding status in the database here
    # Example:
    update_database(source_name, status)

def update_database(source_name, status):
    try:
        latest_entry = rbi_log.objects.using('rbi').filter(source_name=source_name).latest('Sr_no')
        entry, created = rbi_log.objects.using('rbi').filter(source_name=source_name, Sr_no=latest_entry.Sr_no).update_or_create(
            source_name=source_name,
            Sr_no=latest_entry.Sr_no,
            defaults={'source_status': status}
        )
        if not created and entry.source_status != status:
            entry.source_status = status
            entry.save()

    except rbi_log.DoesNotExist:
        rbi_log.objects.using('rbi').create(source_name=source_name, Sr_no=get_unique_sr_no(), source_status=status)
