from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from car_app.models import Car


def index(request):
    response = json.dumps(
        [{'Landing Page': 'Not implemented', 'Available urls': [{'/<car name>': 'To get car details'}]}])
    return HttpResponse(response, content_type='text/json')


def get_car_details(request, car_name):
    if request.method == 'GET':
        try:
            query_set = Car.objects.filter(car_name=car_name).values()
            print(query_set)
            print(type(query_set))
            response = json.dumps(list(query_set))
        except Exception as exc:
            response = json.dumps([{'Error': f'No car found with this name - {car_name}. Error - {exc}'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        try:
            car = Car(car_name=payload['car_name'],
                      brand_name=payload['brand_name'],
                      top_speed=payload['top_speed'],
                      fuel_type=payload['fuel_type'],
                      car_type=payload['car_type'],
                      price=payload['price'])
            car.save()
            response = json.dumps([{'Success': 'Car added successfully!'}])
        except Exception as exc:
            response = json.dumps([{'Error': f'Car could not be added. Error - {exc}'}])

    return HttpResponse(response, content_type='text/json')
