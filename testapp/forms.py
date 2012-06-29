from django import forms
from testapp.models import Survey

class SurveyForm(forms.ModelForm):
    question = forms.Textarea()
    
    class Meta:
        model = Survey
