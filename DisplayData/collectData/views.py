from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
import json

# Create your views here.

def home(request):
    data = models.MyData.objects.first()
    temperature = data.temperature
    moisture = data.moisture
    humidity = data.humidity
    param = {'temperature':temperature, 'moisture':moisture, 'humidity':humidity}
    return render(request, 'collectData/read.html', param)

def getData(request):
    #http://127.0.0.1:8000/getData/?temperature=10&moisture=20&humidity=30
    temperature = request.GET['temperature']
    moisture = request.GET['moisture']
    humidity = request.GET['humidity']
    data = models.MyData.objects.first()
    data.temperature = temperature
    data.moisture = moisture
    data.humidity = humidity
    data.save()
    pump = "ON" if data.pump else "OFF"
    param = {'pump':pump}
    mydata = json.dumps(param)
    return HttpResponse(mydata, content_type='application\json')

def change(request):
    print(request.GET)
    pump = request.GET.get('PUMP',0)
    data = models.MyData.objects.first()
    if pump=="ON":
        data.pump = True
    else:
        data.pump = False
    data.save()
    return redirect("/")

