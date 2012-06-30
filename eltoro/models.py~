from django.db import models
import django.forms as forms

class BudsSurvey(models.Model):
    overall = models.IntegerField()
    overall_comments = models.TextField()
    flavor_wish = models.TextField()
    fav_flav = models.CharField(max_length=500)
    change = models.TextField()
    service = models.IntegerField()
    service_comments = models.TextField()

class BudsSurveyForm(forms.ModelForm):
    choice_list = [(x, x) for x in range(1,6)]
    overall = forms.ChoiceField(choices=choice_list,
                                widget=forms.RadioSelect,
                                initial=3)
    overall_comments = forms.CharField(widget=forms.Textarea)
    flavor_wish = forms.CharField(widget=forms.Textarea)
    fav_flav = forms.CharField()
    change = forms.CharField(widget=forms.Textarea)
    service = forms.ChoiceField(choices=choice_list,
                                widget=forms.RadioSelect,
                                initial=3)
    service_comments = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = BudsSurvey
