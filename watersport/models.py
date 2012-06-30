from django.db import models
import django.forms as forms

class WatersportSurvey(models.Model):

    activity = models.CharField(max_length=100)
    sale = models.CharField(max_length=100, blank=True, null=True)
    instruct = models.IntegerField()
    equipment = models.IntegerField()
    friendly = models.IntegerField()


class WatersportSurveyForm(forms.ModelForm):
    activities = (('water ski', 'water ski'),
               ('wakeboard', 'wakeboard'),
               ('jet ski', 'jet ski'))

    activity = forms.ChoiceField(choices=activities,
                               widget=forms.RadioSelect)

    choices = (('Yes', 'Yes'),
               ('No', 'No'))
   
    sale = forms.ChoiceField(choices=choices,
                             widget=forms.RadioSelect)

    helpful_choices = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    instruct = forms.ChoiceField(choices=helpful_choices,
                                 widget=forms.RadioSelect)
    friendly = forms.ChoiceField(choices=helpful_choices,
                                  widget=forms.RadioSelect)

    equipment  = forms.ChoiceField(choices=helpful_choices,
                                  widget=forms.RadioSelect)

    class Meta:
        model = WatersportSurvey
