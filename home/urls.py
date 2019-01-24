from django.urls import path
from home.views import HomepageView

urlpatterns = [
    path('index.html', HomepageView.as_view()),
]