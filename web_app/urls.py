from django.urls import path
#from django.views.i18n import set_language
from . import views


app_name = 'web'
urlpatterns = [
    path('', views.home, name="home"),
    path('lang/<str:lang_code>/', views.set_lang,name="set_language"),
    path('accounts/profile',views.profile,name="profile"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('submissions/',views.submissions_index,name="submissions_index"),
    #path('set_language/',set_language, name="set_language"),
]
