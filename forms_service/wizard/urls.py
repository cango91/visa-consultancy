from . import views
from django.urls import path

app_name="forms_wizard"
urlpatterns = [
    path("definitions/", views.get_definitions,name="get_definitions"),
    path("definitions/<int:pk>", views.get_definition,name="get_definition"),
    path("fields/", views.get_all_fields,name="get_fields"),
    path("fields/<str:field_type>", views.get_field,name="get_field"),
]