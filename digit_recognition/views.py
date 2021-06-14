from django.shortcuts import render


def index(request):
    context = {}
    print(type(request))
    context['what'] = 'what the'
    print(context)
    # the context will append to the template assigned
    return render(request, 'index.html', context)
