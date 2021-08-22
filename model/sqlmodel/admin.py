from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Stockmarket
# Register your models here.
class DisplayStock(admin.ModelAdmin):
    list_display = ("date","trade_code","open","close","high","low","volume")
    
#admin.site.register(User,)
admin.site.register(Stockmarket,DisplayStock)