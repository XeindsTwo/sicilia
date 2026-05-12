from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

import catalog.views
import users.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog.views.index, name='home'),
    path('login/', users.views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]