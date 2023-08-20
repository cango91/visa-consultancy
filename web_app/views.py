from django.utils import translation
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def home(req):
    user_locale = req.session.get('django_language')
    return render(req,'base.html', {'lang': user_locale})

def set_lang(req, lang_code):
    req.session['django_language'] = lang_code
    return HttpResponseRedirect(req.GET.get('next',req.META.get('HTTP_REFERER', '/')))