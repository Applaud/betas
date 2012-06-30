from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from buds.models import BudsSurvey, BudsSurveyForm

def survey(request):
    errors = False
    if request.method == 'POST':
        form = BudsSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        else:
            errors = True
    else:
        form = BudsSurveyForm()
    return render_to_response('buds/survey.html',
                              {'form': form,
                               'errors': errors},
                              context_instance=RequestContext(request))

def results(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/buds/')
    surveys = BudsSurvey.objects.all()
    avg_experience = sum([s.overall for s in surveys])/float(len(surveys))
    avg_service = sum([s.service for s in surveys])/float(len(surveys))
    return render_to_response('buds/data.html',
                              {'surveys': surveys,
                               'avg_service': avg_service,
                               'avg_experience': avg_experience,
                               'count': len(surveys)},
                              context_instance=RequestContext(request))
