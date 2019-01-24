from django.urls import path
from home.views import HomepageView

urlpatterns = [
    path('about/', HomepageView.as_view()),
]