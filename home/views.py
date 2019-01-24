

# Create your views here.

from django.views import View

class HomepageView(View):
    template_name = "index.html"