from django.shortcuts import render
from django.contrib.sessions.models import Session

# Create your views here.

def landing_page(request):
    return render(request, 'landing_page.html')
    
def visitor_count(request):
    visitor_count = Session.objects.count()
    return {
        'visitor_count': visitor_count,
    }

