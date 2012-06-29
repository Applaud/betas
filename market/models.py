from django.db import models
import django.forms as forms

class MarketSurvey(models.Model):
    general = models.TextField()
    wifi = models.BooleanField()
    reason = models.TextField()
    everything = models.BooleanField()
    beer = models.BooleanField()
    helpful = models.IntegerField()
    friendly = models.IntegerField()
    wish = models.TextField()

class MarketSurveyForm(forms.ModelForm):
    general = forms.CharField(widget=forms.Textarea)
    choices = ((True, 'Yes'),
               (False, 'No'))
    wifi = forms.ChoiceField(choices=choices,
                             widget=forms.RadioSelect)
    reasons = (('grocery', 'grocery'),
               ('drinks', 'drinks'),
               ('breakfast', 'breakfast'),
               ('lunch', 'lunch'))
    reason = forms.ChoiceField(choices=reasons,
                               widget=forms.RadioSelect)
    everything = forms.ChoiceField(choices=choices,
                                   widget=forms.RadioSelect)
    beer = forms.ChoiceField(choices=choices,
                              widget=forms.RadioSelect)
    helpful_choices = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    helpful = forms.ChoiceField(choices=helpful_choices,
                                 widget=forms.RadioSelect)
    friendly = forms.ChoiceField(choices=helpful_choices,
                                  widget=forms.RadioSelect)
    wish = forms.CharField()
    class Meta:
        model = MarketSurvey
