from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_views, name='login'),
    path('logout/', views.logout_views, name='logout'),
]