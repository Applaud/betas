from django.shortcuts import render_to_response

def st_hello(request):
    return render_to_response('welcome.html')
