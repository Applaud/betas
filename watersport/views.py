from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from watersport.models import WatersportSurvey, WatersportSurveyForm

def survey(request):
    errors = False
    if request.method == 'POST':
        form = WatersportSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        else:
            print 'errors'
            errors = True
    else:
        form = WatersportSurveyForm()
    return render_to_response('watersport/survey.html',
                              {'form': form,
                               'errors': errors},
                              context_instance=RequestContext(request))

def results(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/watersport/')
    surveys = WatersportSurvey.objects.all()
    avg_friendly = sum([s.friendly for s in surveys])/float(len(surveys))
    return render_to_response('watersport/data.html',
                              {'surveys': surveys,
                               'count': len(surveys),
                               'avg_friendly': avg_friendly},
                              context_instance=RequestContext(request))
