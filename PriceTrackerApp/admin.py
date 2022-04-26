"""
A module to register data models within the djanog admin site

Inputs: None
"""


from django.contrib import admin
from .models import Vendor, Game, Profile

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Game)
admin.site.register(Profile)
