from django.urls import path

from apps.accounts.views import login_page, logout_user

urlpatterns = [
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
]
