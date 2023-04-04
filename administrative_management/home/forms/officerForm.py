from django import forms
from officers.models import Officer

class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        exclude = ['badge']