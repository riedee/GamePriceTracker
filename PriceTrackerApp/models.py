from django.db import models
from django.contrib import admin
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
    vendorName = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=3)
    freeShipping = models.BooleanField(default=True)
    physicalStore = models.BooleanField(default=False)
    def __str__(self):
        return self.vendorName

class Game(models.Model):
    ACT = 'ACT'
    ADV = 'ADV'
    ACT_ADV = 'ACT_ADV'
    RPG = 'RPG'
    STR = 'STR'
    SIM = 'SIM'
    PZL = 'PZL'
    SPRT = 'SPRT'
    RAC = 'RAC'
    IDL = 'IDL'
    MMO = 'MMO'
    GENRES = ((ACT, 'Action'), (ADV, 'Adventure'), (ACT_ADV, 'Action-Adventure'), 
            (RPG, "Role-Playing"), (STR, "Strategy"), (SIM, "Simulation"), 
            (PZL, 'Puzzle'), (SPRT, 'Sports'), (RAC, 'Racing'), 
            (IDL, 'Idle'), (MMO, 'Massively Multiplayer Online'))
    SW = 'SW'
    PS5 = 'PS5'
    XBXX = 'XBXX'
    PC = 'PC'
    MAC = 'MAC'
    CONSOLES = ((PS5, 'Playstation 5'), (SW, 'Nintendo Switch'), (XBXX, 'XBOX Series X'), (PC, 'PC'), (MAC, 'Mac'))
    gameTitle = models.CharField(max_length=255)
    #genre = models.CharField(max_length=32, choices=GENRES, default=ACT)
    bestVendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default='')
    lowestPrice = MoneyField(max_digits=7, decimal_places=2, default_currency='USD', default = 0)
    url = models.URLField(max_length=500, default = '')
    platform = models.CharField(max_length=32, choices=CONSOLES, default=SW)
    gameID = models.CharField(max_length=100, default = '')
    def __str__(self):
        return self.gameTitle

#Personal information of user
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
    username = models.CharField(max_length=40,default='')
    email = models.CharField(max_length=120,default='')
    fn = models.CharField(max_length=120,default='')
    ln = models.CharField(max_length=120,default='')
    
    def __str__(self):
        return str(self.user_id) + ', ' + str(self.username)
