from django.contrib import admin
from django.urls import path, include

from home import views as home_views
from had import views as had_views
from tests import views as tests_views
from resiliteste import views as resi_views
from burnout import views as burnout_views
from burnoutRotary import views as burn_rot_views
from success import views as suc_views
from authentication.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index, name='home'),
    path('had/', had_views.index, name='had'),
    path('tests/', tests_views.index, name='tests'),
    path('resiliteste', resi_views.index, name='resiliteste'),
    path('burnout/', burnout_views.index, name='burnout'),
    path('burnoutRotary/', burn_rot_views.index, name='burnoutRotary'),
    path('burnoutRotarySuccess/', suc_views.index, name = 'burnoutRotarySuccess'),
    path('login/', login_view, name='login'),
]
