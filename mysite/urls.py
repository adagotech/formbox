"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ninja import NinjaAPI

from formbox.auth_views import router as auth_router
from formbox.settings_views import router as settings_router
from formbox.form_views import router as form_router
from formbox.user_views import router as user_router

api = NinjaAPI()

api.add_router("/auth/", auth_router, tags=['Authentication'])
api.add_router("/settings/", settings_router, tags=['Settings'])
api.add_router("/forms/", form_router, tags=['Forms'])
api.add_router("/users/", user_router, tags=['Users'])

urlpatterns = [
    path('api/', api.urls),
]
