from .views import landing_page
from django.urls import path


urlpatterns = [
    path('', landing_page, name='landing_page'),
]
