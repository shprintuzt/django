from django.http import HttpResponseRedirect
from django.contrib.auth import logout

# Create your views here.
def logged_out(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')