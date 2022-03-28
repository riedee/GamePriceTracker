'''File to enter many users at once into Django'''
from userapp.models import *
from django.contrib.auth.models import User
import csv
import json
#make sure file name is users.csv or change line below to match filename
jsonFile = open('users.json', 'w')
with open('users.csv','rt') as f:
    data = csv.reader(f)
    for row in data:
        user = User()
        user.username= row[0]
        user.set_password= row[1]
        user.first_name = row[2]
        user.last_name = row[3]
        user.email = row[4]
        user.save()
        userDict = {'username': row[0], 'password': row[1], 'fn': row[2], 'ln': row[3], 'email': row[4]}
        json.dump(userDict, jsonFile)
