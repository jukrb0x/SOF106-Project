from django.shortcuts import render, HttpResponse

import time


def index(request):
    """
    The index page handler
    :param request:
    :return:
    """
    context = {}
    _type = "Type of request: " + str(type(request))
    print(_type)
    context['time'] = time.asctime(time.localtime(time.time()))
    print("Context Dict: " + str(context))
    # eject the context to the template
    return render(request, 'index.html', context)


def api(request):
    """
    API root page handler
    :param request:
    :return:
    """
    api_html_template = """
    <html><body><pre>Welcome to API root</pre></body></html>
    """
    return HttpResponse(api_html_template)
