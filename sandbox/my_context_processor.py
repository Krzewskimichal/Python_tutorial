from django.contrib.auth.models import Group


def is_logged(request):
    if request.user.is_authenticated:
        return request.user.username


def my_cp(request):

    ctx = {
        'username': is_logged(request),

    }
    return ctx
