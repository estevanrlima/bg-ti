from django.contrib import admin
from django.urls import path

from home import views as home_views
from had import views as had_views
from tests import views as tests_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index),
    path('had/', had_views.index),
    path('tests/', tests_views.index)
]
