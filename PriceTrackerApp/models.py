from django.db import models
from djmoney.models.fields import MoneyField
from userapp import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Vendor(models.Model):
    vendorName = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(default=3)
    freeShipping = models.BooleanField(default=True)
    physicalStore = models.BooleanField(default=False)
    storeFront = models.URLField(max_length=500, default = '')
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
    #bestVendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, default='')
    bestVendor = models.CharField(max_length=100, default='')
    lowestPrice = MoneyField(max_digits=7, decimal_places=2, default_currency='USD', default = '0')
    url = models.URLField(max_length=500, default = '')
    platform = models.CharField(max_length=32, default=SW)
    gameID = models.CharField(max_length=100, default = '')
    def __str__(self):
        return self.gameTitle

class UserGame(models.Model):
    userGameID = models.CharField(max_length=100, default = '')
    gameID = models.CharField(max_length=100, default = '')
    userID = models.CharField(max_length=100, default = '')
    
#Profile information of user
class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=40,default='')
    email = models.CharField(max_length=120,default='')
    fn = models.CharField(max_length=120,default='')
    ln = models.CharField(max_length=120,default='')
    #saved_game = models.CharField(max_length=120, default='')
    saved_game = models.ForeignKey(Game, db_index=True, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user_id.username

#NOTE: will only proc when adding new users to the database, i.e. existing users do not have profiles
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_id=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()