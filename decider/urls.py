from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from api import views
from django.views.generic import RedirectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'starterdecks', views.StarterDeckViewSet)
router.register(r'cards', views.CardViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', RedirectView.as_view(url='index/')),
  path('index/', views.index, name='home'),
  path('api', views.names),
  path('accounts/', include('allauth.urls')),
  path('decks/', views.decks, name='decks'),
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  path('confetti/', views.confetti, name='confetti'),
]