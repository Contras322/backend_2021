from django.http import HttpResponseRedirect
from rest_framework.request import Request
from django.shortcuts import render


def user_id_auth(fun):
    def wrapper(*args, **kwargs):
        is_auth = False
        if isinstance(args[0], Request):
            is_auth = args[0].user.is_authenticated
        else:
            is_auth = args[1].user.is_authenticated

        if not is_auth:
            return HttpResponseRedirect('/auth/')

        return fun(*args, **kwargs)

    return wrapper


def auth(request):
    return render(request, 'login.html')
