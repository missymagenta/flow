from django.http import HttpResponse
from django.views import View


class RegistrationView(View):

    def post(self, request):
        user_email = request.POST.get("email")
        user_password = request.POST.get("psw")
        print(f"We saved the email {user_email} and password {user_password}")
        return HttpResponse()




