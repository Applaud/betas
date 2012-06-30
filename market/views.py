from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from market.models import MarketSurvey, MarketSurveyForm

def survey(request):
    errors = False
    if request.method == 'POST':
        form = MarketSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
        else:
            errors = True
    else:
        form = MarketSurveyForm()
    return render_to_response('market/survey.html',
                              {'form': form,
                               'errors': errors},
                              context_instance=RequestContext(request))

def results(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/market/')
    surveys = MarketSurvey.objects.all()
    if len(surveys) is not 0:
        avg_friendly = sum([s.friendly for s in surveys])/float(len(surveys))
        avg_helpful = sum([s.helpful for s in surveys])/float(len(surveys))
        print "hello"
    else:
        print "goodbye"
        avg_friendly = 0
        avg_helpful = 0
    return render_to_response('market/data.html',
                              {'surveys': surveys,
                               'count': len(surveys),
                               'avg_friendly': avg_friendly,
                               'avg_helpful': avg_helpful},
                              context_instance=RequestContext(request))
