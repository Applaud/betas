from django.db import models
import django.forms as forms

class MarinaSurvey(models.Model):
    general = models.TextField()
    service = models.TextField()
    storage = models.BooleanField()
    boat = models.BooleanField()
    helpful = models.IntegerField()
    friendly = models.IntegerField()
    wish = models.TextField()

class MarinaSurveyForm(forms.ModelForm):
    general = forms.CharField(widget=forms.Textarea)

    services = (('fuel dock', 'fuel dock'),
               ('launch ramp', 'launch ramp'),
               ('travel lift', 'travel lift'),
               ('fork lift', 'fork lift'),
               ('mechanical', 'mechanical'))

    service = forms.ChoiceField(choices=services,
                               widget=forms.RadioSelect)

    choices = ((True, 'Yes'),
               (False, 'No'))
   

    storage = forms.ChoiceField(choices=choices,
                             widget=forms.RadioSelect)

    boat = forms.ChoiceField(choices=choices,
                             widget=forms.RadioSelect)
    
    helpful_choices = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    helpful = forms.ChoiceField(choices=helpful_choices,
                                 widget=forms.RadioSelect)
    friendly = forms.ChoiceField(choices=helpful_choices,
                                  widget=forms.RadioSelect)
    wish = forms.CharField()
    class Meta:
        model = MarinaSurvey
