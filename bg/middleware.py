from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the URL parameter is present
        if ('allow_access' in request.GET and request.path == '/burnoutRotarySuccess/') or ('allow_access' in request.GET and request.path == '/burnoutRotary/'):           
            # Skip the middleware and allow access
            return self.get_response(request)


        # Check if the user is authenticated
        if not request.user.is_authenticated and request.path != reverse('login'):
            # Redirect the user to the login page
            #login_url = reverse('login')
            return redirect('login')

        return self.get_response(request)
