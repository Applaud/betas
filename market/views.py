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
        return HttpResponseRedirect('/coffeeand/')
    surveys = MarketSurvey.objects.all()
    avg_friendly = sum([s.friendly for s in surveys])/float(len(surveys))
    avg_helpful = sum([s.helpful for s in surveys])/float(len(surveys))
    return render_to_response('coffeeand/data.html',
                              {'surveys': surveys,
                               'count': len(surveys),
                               'avg_friendly': avg_friendly,
                               'avg_helpful': avg_helpful},
                              context_instance=RequestContext(request))
