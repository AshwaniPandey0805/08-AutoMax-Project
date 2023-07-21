from django.urls import path
from .views import login_view, ReisterView

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path("register/", ReisterView.as_view(), name="register")
    
]
