import json

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import HttpResponse


def image_handler(request: WSGIRequest):
    """
    The function receives an image base64 data and
    handle it to the recognition process,
    return the result number with probability.
    ------
    * I did not write the data validity for requests, I should refine that someday.
    """
    if request.method == 'POST':
        # for debugging usage
        print(request)
        print(
            "\nrequest.path: ", request.path,
            "\nrequest.body: ", request.body,
            "\nrequest.META: ", request.META,
            "\nrequest.path_info: ", request.path_info,
            "\nrequest.COOKIES: ", request.COOKIES,
        )

        # TODO: handle recognition here

        # response json data
        res = json.dumps({
            'number': 0,
            'probability': 0
        })
        # return the data
        return HttpResponse(res)
    if request.method == 'GET':
        # for debugging usage
        print(request)
        print(
            "\nrequest.path: ", request.path,
            "\nrequest.body: ", request.body,
            "\nrequest.META: ", request.META,
            "\nrequest.path_info: ", request.path_info,
            "\nrequest.COOKIES: ", request.COOKIES,
        )
        # do nothing here
        return HttpResponse("AAh Oh.. seems you get the wrong place!")
