from django.contrib import admin
from nutshell.api.models import Manufacturer, Shoe, ShoeColor, ShoeType 

admin.site.register(Manufacturer)
admin.site.register(Shoe)
admin.site.register(ShoeColor)
admin.site.register(ShoeType)

