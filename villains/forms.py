from django import forms
from .models import Villain

class VillainForm(forms.ModelForm):
    class Meta:
        model = Villain
        fields = "__all__"
    
# Luiz Enrique