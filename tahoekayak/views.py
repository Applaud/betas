from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from tahoekayak.models import TahoeKayakSurvey, TahoeKayakSurveyForm

def survey(request):
    errors = False
    if request.method == 'POST':
        form = TahoeKayakSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        else:
            errors = True
    else:
        form = TahoeKayakSurveyForm()
    return render_to_response('tahoekayak/survey.html',
                              {'form': form,
                               'errors': errors},
                              context_instance=RequestContext(request))
def results(request):
#    if not request.user.is_authenticated():
#        return HttpResponseRedirect('/kayak/')
    surveys = TahoeKayakSurvey.objects.all()
    avg_enjoyable = sum([s.enjoyable for s in surveys])/float(len(surveys))
    avg_guide = sum([s.guide for s in surveys])/float(len(surveys))
    avg_booking = sum([s.booking for s in surveys])/float(len(surveys))
    avg_transport = sum([s.transport for s in surveys])/float(len(surveys))
    return render_to_response('tahoekayak/data.html',
                              {'surveys': surveys,
                               'count': len(surveys),
                               'avg_transport': avg_transport,
                               'avg_booking': avg_booking,
                               'avg_guide': avg_guide,
                               'avg_enjoyable': avg_enjoyable},
                              context_instance=RequestContext(request))
