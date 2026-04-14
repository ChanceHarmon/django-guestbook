from django import forms
from .models import VisitorEntry

class VisitorEntryForm(forms.ModelForm):
    class Meta:
        model = VisitorEntry
        fields = ["name", "message"]

