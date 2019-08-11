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
  path('', views.decks, name='decks'),
  path('index/', views.index, name='info'),
  # path('accounts/', include('allauth.urls')),
  # path('', include(router.urls)),
  # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]