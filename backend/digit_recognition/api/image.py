from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import HttpResponse


def image_handler(request: WSGIRequest):
    if request.method == 'POST':
        print(request)
        print(request.body)
        return HttpResponse(200)
    return HttpResponse(200)
