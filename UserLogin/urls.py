from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name="Register"),
    path('login/', views.Login.as_view(), name="Login"),
    path('logout/', views.Logout.as_view(), name="Logout"),
    path('dashboard/<int:id>/', views.Dashboard.as_view(), name="Dashboard"),
    path('first/', views.First.as_view(), name="First"),
    path('second/', views.Second.as_view(), name="Second"),
    path('third/', views.Third.as_view(), name="Third"),
    path('fourth/', views.Fourth.as_view(), name="Fourth"),
    path('pdf/<int:id>/', views.PDF.as_view(), name="PDF"),
    path('otp/<str:email>/', views.OTP.as_view(), name="OTP"),
]
