from django.shortcuts import render, HttpResponse

import time


def index(request):
    """
    The index page handler
    :param request:
    :return:
    """
    context = {'time': time.asctime(time.localtime(time.time()))}
    _type = "Type of request: " + str(type(request))
    print(_type)
    print("Context Dict: " + str(context))
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
    ret = api_html_template
    return HttpResponse(ret)


def api_root_test_handler(request):
    context = {'time': time.asctime(time.localtime(time.time()))}
    return render(request, 'api-tester.html', context)
