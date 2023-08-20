from django.conf import settings

def flags(request):
    return {'FLAGS': settings.FLAGS}