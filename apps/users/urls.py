from django.urls import path

from .views import RegisterUserView

register = {
    'post': 'post',
}

urlpatterns = [
    path('register/', RegisterUserView.as_view(register), name="register-user"),
]


