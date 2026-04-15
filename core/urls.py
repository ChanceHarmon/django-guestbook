from django.urls import path
from .views import accept_req, list_visitors, render_homepage, delete_entry

urlpatterns = [path("hello/", accept_req), path("visitors/", list_visitors), path("delete/<int:entry_id>/", delete_entry, name="delete_entry")]

