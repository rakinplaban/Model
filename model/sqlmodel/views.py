from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Stockmarket
# Create your views here.

def index(request):
    stock = Stockmarket.objects.all()
    return render(request,"sqlmodel/index.html",{
        "stock" : stock
    })

def edit(request):
    if request.method == "POST":
        trade_code = request.POST['trade_code']
        date = request.POST['date']
        open = request.POST['open']
        close = request.POST['close']
        high = request.POST['high']
        low = request.POST['low']
        volume = request.POST['volume']
        stockmarketdata = Stockmarket(trade_code = trade_code, date = date, open = open, close = close, high=high, low = low, volume=volume)
        stockmarketdata.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request,"sqlmodel/edit.html")