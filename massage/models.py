from django.db import models
import django.forms as forms
from django.forms import ModelForm

class MassageSurvey(models.Model):
    fav_part = models.CharField(max_length=100)
    music = models.CharField(max_length=100)
    new_oils = models.CharField(max_length=100)
    extend = models.CharField(max_length=500)

class MassageSurveyForm(forms.ModelForm):
    fav_part = forms.CharField()
    music = forms.CharField()
    oil_choices = [('lavender','lavender'),
                   ('peppermint', 'peppermint'),
                   ('rosebud', 'rosebud'),
                   ('cinnamon', 'cinnamon')]
    new_oils = forms.ChoiceField(choices=oil_choices,
                                  widget=forms.RadioSelect)
    extend_choices = [('not really', 'not really'),
                      ('yes - by 15 mins','yes - by 15 mins'),
                      ('yes - by 30 mins', 'yes - by 30 mins')]
    extend = forms.ChoiceField(choices=extend_choices,
                               widget=forms.RadioSelect)
    class Meta:
        model = MassageSurvey
