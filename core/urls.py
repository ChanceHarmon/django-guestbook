from django.urls import path
from .views import list_visitors, delete_entry

urlpatterns = [path("visitors/", list_visitors), path("delete/<int:entry_id>/", delete_entry, name="delete_entry")]

