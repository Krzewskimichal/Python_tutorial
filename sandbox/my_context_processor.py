from sandbox.models import UserFeature


def is_logged(request):
    if request.user.is_authenticated:
        return request.user.username


def get_level(request):
    id = request.user.id
    user = UserFeature.objects.filter(user_id=id).first()
    return user.level if user else 1


def my_cp(request):

    ctx = {
        'username': is_logged(request),
        'level': get_level(request),
    }
    return ctx
