from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.http import HttpResponse



def allow_users(authorized_users=[]):

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists:
                group = request.user.groups.all()
                for grp in group:
                    if grp.name in authorized_users:
                        return view_func(request, *args, **kwargs)
                    else:
                        return HttpResponse('<h1>You are not allowed here</h1>')
        return wrapper_func
    return decorator

