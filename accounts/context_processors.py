from accounts.models import User


def owner(request):
    return {'owner': User.objects.filter(is_owner=True).first()}
