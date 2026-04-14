from django.urls import path
from .views import accept_req, list_visitors, render_homepage

urlpatterns = [path("hello/", accept_req), path("visitors/", list_visitors)]

