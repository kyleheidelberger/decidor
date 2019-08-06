from django.shortcuts import render
from django.http import JsonResponse
from api.models import StarterDeck, Card
from rest_framework import viewsets
from api.serializers import StarterDeckSerializer, CardSerializer


class StarterDeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows StarterDecks to be viewed or edited.
    """
    queryset = StarterDeck.objects.all()
    serializer_class = StarterDeckSerializer


class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

def decks(request):
    return render(request, 'decks.html')