from api.models import StarterDeck, Card
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = ['title', 'card_image', 'description', 'deck', 'url']

class StarterDeckSerializer(serializers.ModelSerializer):
    card_set = CardSerializer(many=True, read_only=True)
    class Meta:
        model = StarterDeck
        fields = ['title', 'deck_image', 'card_set']
        read_only_fields = ['title', 'deck_image', 'card_set']


