from django.urls     import path
from users.views     import SignupViewSet
from rest_auth.views import LoginView

urlpatterns = [
    path('/signup', SignupViewSet.as_view()),
    path('/login', LoginView.as_view()),
]