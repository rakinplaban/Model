#from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#class User(AbstractUser):
    #pass

class Stockmarket(models.Model):
    
    trade_code = models.TextField()
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"date:{self.date} trade_code:{self.trade_code} open:{self.open} close:{self.close} high:{self.high} low{self.low}"