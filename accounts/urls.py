from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('lessor_dashboard', views.lessor_dashboard, name='lessor_dashboard'),
    path('lessee_dashboard', views.lessee_dashboard, name='lessee_dashboard')
]
