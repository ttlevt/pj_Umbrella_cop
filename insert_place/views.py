#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from run_ import cross_v
from django.http import JsonResponse
import request
# import requeststype
import requests

# from urllib import parse
# Create your views here.

# def index(request):
#     result = cross_v(request)
#     return HttpResponse(result)
def home(requests):
    print('req_encoding:::::',requests.encoding)
    print('requeststype:', type(requests))
    print('request!!!!!:', requests)
    place_name = request.GET['name']
    print('place_name::::::', place_name)

    result = cross_v(place_name)
    return JsonResponse(result, safe = False)