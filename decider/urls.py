from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from api import views
from django.views.generic import RedirectView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', RedirectView.as_view(url='index/')),
  # url(r'^$', TemplateView.as_view(template_name='index.html')),
  path('index/', views.index, name='home'),
  path('api', views.names),
  # path('accounts/', include('registration.backends.default.urls')),
  path('accounts/', include('allauth.urls')),
  path('decks/', views.decks, name='decks'),
]