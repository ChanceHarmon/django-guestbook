from django import forms
from .models import VisitorEntry

class VisitorEntryForm(forms.ModelForm):
    class Meta:
        model = VisitorEntry
        fields = ["name", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your name"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Leave a message...",
                "rows": 4
            }),
        }
