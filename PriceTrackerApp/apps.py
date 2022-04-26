"""
A django app to register the app PriceTrackerApp with the project
Inputs: AppConfig
"""

from django.apps import AppConfig


class PricetrackerappConfig(AppConfig):
    """Configure the app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PriceTrackerApp'
