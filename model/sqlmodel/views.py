from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Stockmarket
from .forms import stock_form
# Create your views here.

def index(request):
    stock = Stockmarket.objects.all()
    return render(request,"sqlmodel/index.html",{
        "stock" : stock
    })

def edit(request):
    form = stock_form()
    if request.method == "POST":
        form = stock_form(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(reverse("index"))
        return render(request,"sqlmodel/edit.html",{
            "form" : form
        })
    return render(request,"sqlmodel/edit.html",{
        "form" : form
    })
def editdata(request,id):
    display = Stockmarket.objects.get(pk = id)
    form = stock_form(instance = display)
    if request.method == "POST":
        form = stock_form(request.POST,instance=display)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            stockmarketdata = Stockmarket(id=instance.id,trade_code = instance.trade_code, date = instance.date, open = instance.open, close = instance.close, high=instance.high, low = instance.low, volume=instance.volume)
            stockmarketdata.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request,"sqlmodel/edit.html",{
        "display" : display,
        "form" : form
    })

def deletedata(request,id):
    display = Stockmarket.objects.get(pk = id)
    display.delete()
    return HttpResponseRedirect(reverse("index"))