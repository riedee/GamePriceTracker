from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.

class User(models.Model):
    username = models.SlugField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length = 254)

class Vendor(models.Model):
    vendorName = models.CharField(max_length=255)
    linkToStore = models.URLField(max_length=200)
    rating = models.PositiveSmallIntegerField(default=3)
    freeShipping = models.BooleanField(default=True)
    price = MoneyField(max_digits=11, decimal_places=2, default_currency='USD')
    def __str__(self):
        return self.vendorName, self.price, self.linkToStore


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
    genre = models.CharField(max_length=32, choices=GENRES, default=ACT)
    vendorInfo = models.ManyToManyField(Vendor)
    def __str__(self):
        return self.gameTitle