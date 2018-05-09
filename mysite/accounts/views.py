from django.shortcuts import render

# Create your views here.

def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'mysite/login_error.html')