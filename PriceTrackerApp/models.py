from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.
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
    GME = 'GME'
    STM = 'STM'
    AMZN = 'AMZN'
    PSN = 'PSN'
    MSFT = 'MSFT'
    NTDOY = 'NTDOY'
    TGT = 'TGT'
    WMT = 'WMT'
    VENDORS = ((GME, 'GameStop'), (STM, 'Steam'), (AMZN, 'Amazon'), (PSN, 'Playstation Store'),
                (MSFT, 'Microsoft Store'), (NTDOY, 'Nintendo eShop'), (TGT, 'Target'), (WMT, 'Walmart'))
    SW = 'SW'
    PS5 = 'PS5'
    XBXX = 'XBXX'
    PC = 'PC'
    MAC = 'MAC'
    CONSOLES = ((PS5, 'Playstation 5'), (SW, 'Nintendo Switch'), (XBXX, 'XBOX Series X'), (PC, 'PC'), (MAC, 'Mac'))
    name = models.CharField(max_length=255)
    price = MoneyField(decimal_places=2, default=0, default_currency='USD', max_digits=11)
    genre = models.CharField(max_length=32, choices=GENRES, default=ACT)
    vendor = models.CharField(max_length=32, choices=VENDORS, default=AMZN)
    console = models.CharField(max_length=32, choices=CONSOLES, default=SW)
