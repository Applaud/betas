from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.forms.formsets import formset_factory
from testapp.models import Survey, Response
from testapp.forms import SurveyForm
import json

class SurveyEncoder(json.JSONEncoder):
    """Allows us to JSON serialize a Survey."""
    
    def default(self, o):
        if isinstance(o, Survey):
            l = o.questions
            l.append(o.title)
            return l
        else:
            return json.JSONEncoder.default(self, o)

def send_surveys(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps(list(Survey.objects.all()), cls=SurveyEncoder),
                            mimetype='application/json')
    else:
        return HttpResponse(jsons.dumps('failure!'), mimetype='application/json')

# should do checking to avoid possible exceptions with bad JSON data
def receive_response(request):
    if request.method == 'POST':
        request_data = json.load(request)
        answers = request_data['answers'];
        survey = request_data['survey'];
        response = Response(answers=answers, survey=survey)
        response.save()
        return HttpResponse("success!")
    return HttpResponse("failure!")

def all_surveys(request):
    if request.user.is_authenticated():
        return render_to_response('surveys.html',
                                  {'surveys': list(Survey.objects.all())},
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

# TODO: fix this and survey_form.html so that form content isn't discarded on error

def form_create(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    if request.method == 'GET':
        return render_to_response('testapp/survey_form.html',
                                  {},
                                  context_instance=RequestContext(request))
    if request.method == 'POST':
        i = 0
        questions = []
        while 'area_' + str(i) in request.POST and request.POST['area_' + str(i)]:
            questions.append(request.POST['area_' + str(i)])
            i += 1
        title = ''
        if 'title' in request.POST and request.POST['title']:
            title = request.POST['title']
        errors = {}
        err = False
        if not title:
            errors['title_err'] = "You should enter a title for your survey."
            err = True
        if not questions:
            errors['questions_err'] = "No questions?"
            err = True
        if err:
            errors['questions'] = questions
            return render_to_response('testapp/survey_form.html',
                                      errors,
                                      context_instance=RequestContext(request))
        survey = Survey(title=title, questions=questions)
        survey.save()
        return HttpResponseRedirect('results')

def all_responses(request):
    if request.user.is_authenticated():
        responses = Response.objects.order_by('survey')
        return render_to_response('testapp/response.html',
                                  {'responses': responses},
                                  context_instance=RequestContext(request))
    return HttpResponseRedirect('/login')
