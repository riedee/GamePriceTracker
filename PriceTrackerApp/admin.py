from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Vendor)
admin.site.register(VendorPrice)
admin.site.register(VendorURL)
admin.site.register(Game)

