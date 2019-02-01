from django.urls import path
from registration.views import RegistrationView

urlpatterns = [
    path('success', RegistrationView.as_view()),
]
