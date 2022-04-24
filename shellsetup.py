#we can mess around with the data and test the data
#when importing: import shell_setup.py
#
from django.db import models
from django.contrib.auth.models import User
from PriceTrackerApp.models import Game, Vendor, Profile
users = User.objects.all()
games = Game.objects.all()
vendors = Vendor.objects.all()
profiles = Profile.objects.all()
print("this file imported django models, users, and PriceTrackerApp.models: Game and Vendor")
print("This file defined the following variables: users, games, vendors")
