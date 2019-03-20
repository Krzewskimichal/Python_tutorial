from sandbox.models import UserFeature


def is_logged(request):
    if request.user.is_authenticated:
        return request.user.username


def get_level(request):
    id = request.user.id
    user = UserFeature.objects.filter(user_id=id).first()
    return user.level if user else 1


def is_admin(request):
    if request.user.is_superuser:
        return True


def my_cp(request):

    ctx = {
        'admin': is_admin(request),
        'username': is_logged(request),
        'level': get_level(request),
    }
    return ctx
