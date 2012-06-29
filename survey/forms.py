from django.forms import ModelForm, ChoiceField, CharField, Textarea, RadioSelect, Form, PasswordInput
from survey.models import Survey

class SurveyForm(ModelForm):
    drink = CharField(required=False)
    choice_list = [(x, x) for x in range(1,6)]
    choice_list.append((-1,'n/a'))
    rating = ChoiceField(choices=choice_list,
                         widget=RadioSelect, required=False, initial=-1)
    drink_comment = CharField(required=False,widget=Textarea(attrs={'rows':2}))
    music = CharField(required=False,widget=Textarea(attrs={'rows':2}))
    change = CharField(required=False,widget=Textarea(attrs={'rows':2}))
    comment = CharField(required=False,widget=Textarea(attrs={'rows':2}))
    class Meta:
        model = Survey

class LoginForm(Form):
    username = CharField(label='Username')
    password = CharField(widget=PasswordInput, label='password')
