from django import forms
from citations.models import Citation

class CitationForm(forms.ModelForm):
    class Meta:
        model = Citation
        exclude = ['violationDate','violationTime','officer']