from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def myview(request):
    template = loader.get_template('myview.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logged_out(request):
    logout(request)
    return HttpResponseRedirect('/accounts/')