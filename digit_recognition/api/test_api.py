from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse
import requests


def test_api(request: WSGIRequest):
    print(type(request))
    if request:
        print(request)

    return HttpResponse(200)
