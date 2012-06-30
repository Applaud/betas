from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from eltoro.models import EltoroSurvey, EltoroSurveyForm

def survey(request):
    errors = False
    if request.method == 'POST':
        form = EltoroSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        else:
            errors = True
    else:
        form = EltoroSurveyForm()
    return render_to_response('eltoro/survey.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def results(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/eltoro/')
    surveys = EltoroSurvey.objects.all()
    return render_to_response('eltoro/data.html',
                              {'surveys': surveys,
                               'count': len(surveys)},
                              context_instance=RequestContext(request))
