from django.db import models
import django.forms as forms

class EltoroSurvey(models.Model):
    margarita = models.TextField()
    missing = models.TextField()
    best = models.TextField()
    beer = models.TextField()
    time = models.TextField()
    place = models.TextField()

class EltoroSurveyForm(forms.ModelForm):
    margarita = forms.CharField()
    missing  = forms.CharField()
    best = forms.CharField()
    beer = forms.CharField()
    time  = forms.CharField()
    place = forms.CharField()
    
    class Meta:
        model = EltoroSurvey



