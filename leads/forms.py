from django import forms
from .models import lead

class LeadModelForm(forms.ModelForm):
    class Meta:
        model=lead
        fields =(
            'first_name',
            'last_name',
            'age',
            'agent',
        )


 