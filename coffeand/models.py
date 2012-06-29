from django.db import models
import django.forms as forms

class CoffeeAndSurvey(models.Model):
    service = models.IntegerField()
    service_comment = models.TextField()
    eggs = models.IntegerField()
    favorite = models.TextField()
    different = models.TextField()
    overall = models.IntegerField()
    overall_comment = models.TextField()

class CoffeeAndSurveyForm(forms.ModelForm):
    choice_list = [(x, x) for x in range(1,6)]
    eggs_list = ((1, 'Yes, serve eggs benedict!'),
                 (0, 'No, not so interested.'))
    service = forms.ChoiceField(choices=choice_list,
                                widget=forms.RadioSelect,
                                initial=3)
    service_comment = forms.CharField(widget=forms.Textarea)
    eggs = forms.ChoiceField(choices=eggs_list,
                                widget=forms.RadioSelect,
                                initial=1)
    favorite = forms.CharField(widget=forms.Textarea)
    different = forms.CharField(widget=forms.Textarea)
    overall = forms.ChoiceField(choices=choice_list,
                                widget=forms.RadioSelect,
                                initial=3)
    overall_comment = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = CoffeeAndSurvey
