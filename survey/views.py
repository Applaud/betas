from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from survey.models import Survey, HitCount
from survey.forms import SurveyForm, LoginForm

def thanks(request):
    return render_to_response('thanks.html',
                              {},
                              context_instance=RequestContext(request))

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = SurveyForm()
        counter = HitCount.objects.all()[0]
        counter.count += 1
        counter.save()
    return render_to_response('survey.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def results(request):
    if request.user.is_authenticated():
        surveys = list(Survey.objects.all())
        rating_total = 0
        num_ratings = 0
        for survey in surveys:
            if survey.rating == -1:
                survey.rating = 'n/a'
            if 0 <= survey.rating <= 5:
                rating_total += survey.rating
                num_ratings += 1
        # Nasty-looking floating point arithmetic here to truncate floats to two decimal places.
        # There might be a more concise way to do it.
        return render_to_response('data.html',
                                  {'surveys': surveys,
                                   'hit_count': HitCount.objects.all()[0].count,
                                   'response_count': len(surveys),
                                   'ratio': int(float(len(surveys))*100)/HitCount.objects.all()[0].count,
                                   'avg': int(float(rating_total)*100/num_ratings)/100.0,
                                   },
                                  context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def login(request):
    if request.user.is_authenticated():
        return render_to_response('landing.html')
    else:
        error = False
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = auth.authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return render_to_response('landing.html')
                else:
                    error = True
        else:
            form = LoginForm()
            error = True
    return render_to_response('login.html',
                              {'form': form,
                               'error': error},
                              context_instance=RequestContext(request))
