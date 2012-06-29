from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from coffeand.models import CoffeeAndSurvey, CoffeeAndSurveyForm

def survey(request):
    errors = False
    if request.method == 'POST':
        form = CoffeeAndSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        else:
            errors = True
    else:
        form = CoffeeAndSurveyForm()
    return render_to_response('coffeeand/survey.html',
                              {'form': form,
                               'errors': errors},
                              context_instance=RequestContext(request))

def results(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/coffeeand/')
    surveys = CoffeeAndSurvey.objects.all()
    avg_service = sum([s.service for s in surveys])/float(len(surveys))
    avg_overall = sum([s.overall for s in surveys])/float(len(surveys))
    return render_to_response('coffeeand/data.html',
                              {'surveys': surveys,
                               'count': len(surveys),
                               'avg_overall': avg_overall,
                               'avg_service': avg_service},
                              context_instance=RequestContext(request))
