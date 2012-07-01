from django.db import models
import django.forms as forms

class TahoeKayakSurvey(models.Model):
    favorite = models.TextField()
    enjoyable = models.IntegerField()
    guide = models.IntegerField()
    booking = models.IntegerField()
    transport = models.IntegerField()
    comments = models.TextField()

class TahoeKayakSurveyForm(forms.ModelForm):
    choice_list = [(x, x) for x in xrange(1,6)]
    favorite = forms.CharField()
    enjoyable = forms.ChoiceField(choices=choice_list,
                                  widget=forms.RadioSelect,
                                  initial=3)
    guide = forms.ChoiceField(choices=choice_list,
                                  widget=forms.RadioSelect,
                                  initial=3)
    booking = forms.ChoiceField(choices=choice_list,
                                  widget=forms.RadioSelect,
                                  initial=3)
    transport = forms.ChoiceField(choices=choice_list,
                                  widget=forms.RadioSelect,
                                  initial=3)
    comments = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = TahoeKayakSurvey
