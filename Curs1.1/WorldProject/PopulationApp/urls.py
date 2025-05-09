from django.urls import path
from .views import all_countries_view

urlpatterns = [

	path("all", all_countries_view),
]
