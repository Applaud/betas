from django.db import models
import json

class SerializedStringsField(models.TextField):
    """Allows us to store a list of strings
    directly in the database using JSON to
    serialize/deserialize."""
    
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(SerializedStringsField, self).__init__(*args, **kwargs)
    
    def to_python(self, value):
        if not value:
            return
        if isinstance(value, list):
            return value
        return json.loads(value)
    
    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return json.dumps(value)

class Response (models.Model):
    """Contains a response to a particular survey.
    self.survey gives the title of the survey to 
    which this is a response to. self.answers 
    contains the list of answers to said survey."""
    
    answers = SerializedStringsField()
    survey = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "Survey: '%s'; Answers: %s" % (self.survey, self.answers)

class Survey (models.Model):
    
    title = models.CharField(max_length=100)
    questions = SerializedStringsField()
    
    def __unicode__(self):
        return "title: %s; questions: %s" % (self.title, self.questions)
