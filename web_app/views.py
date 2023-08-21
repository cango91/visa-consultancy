from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.

def home(req):
    user_locale = req.session.get('django_language')
    return render(req,'home.html', {'lang': user_locale})

def set_lang(req, lang_code):
    req.session['django_language'] = lang_code
    return HttpResponseRedirect(req.GET.get('next',req.META.get('HTTP_REFERER', '/')))

@login_required
def profile(req):
    return redirect(reverse('web:home'))

@login_required
def dashboard(req):
    return redirect(reverse('web:home'))

@login_required
def submissions_index(req):
    return redirect(reverse('web:home'))