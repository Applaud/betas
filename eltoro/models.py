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
    class Meta:
        model = EltoroSurvey



