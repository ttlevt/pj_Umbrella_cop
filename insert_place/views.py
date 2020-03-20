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
def home(request):

    # print('req_encoding:::::', request.encoding)
    # print('requeststype:', type(request))
    # print('request!!!!!:', request)
    place_name = request.GET['name']
    # print('place_name::::::', place_name)


    place_name = request.GET['name']
    result = cross_v(place_name)
    return JsonResponse(result, safe=False)




    # print('place_name::::::', place_name)
    # print('req_encoding:::::', request.encoding)
    # print('requeststype:', type(request))
    # print('request!!!!!:', request)
