import base64
import json
import os
from io import BytesIO
import numpy as np
import tensorflow as tf

from PIL import Image
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import HttpResponse
from numpy import ndarray
from ..trainer import predict


def image_handler(request: WSGIRequest):
    """
    The function receives an image base64 data and
    handle it to the recognition process,
    return the result number with probability.
    ------
    Args:
        request (WSGIRequest): the data contains a form of imgValue
            imgValue: image data64 code
    Returns:
        HttpResponse (HttpResponse): a json form consist of result
            {
                number: 'str'
                probability: 'str'
            }
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

        # load requests to json dict
        req = json.loads(request.body, encoding='utf-8')
        # initiate predict for request data
        prediction = predict.Predict(req['imgValue'])
        prediction.base64_to_image()
        prediction.predict()

        # response json data
        res = json.dumps({
            'number': str(prediction.digit),
            # FIXME: probability
            'probability': '0'
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
