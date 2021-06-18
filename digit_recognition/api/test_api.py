from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse
import requests

"""
Receive data: image

"""

# Test API to handle POST data
def test(request: WSGIRequest):
    print(type(request))
    if request:
        print(request)
    return HttpResponse(200)
