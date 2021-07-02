from __future__ import annotations

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse

import time


def index(request):
    """
    The index page handler
    :param request:
    :return:
    """
    context = {'time': time.asctime(time.localtime(time.time()))}
    # eject the context to the template
    return render(request, 'index.html', context)


def api_root_handler(request):
    """
    API root page handler
    :param request:
    :return:
    """
    api_html_template = """
    <html><body><pre>Welcome to API root</pre></body></html>
    """
    _type = "Type of request: " + str(type(request))
    print(_type)
    ret = api_html_template
    if request.method == 'POST':
        return HttpResponse(ret)
    else:
        return HttpResponse(ret)
