from api.models import StarterDeck, Card
from rest_framework import serializers

class StarterDeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StarterDeck
        fields = ['title', 'deck_image']


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['title', 'description', 'deck', 'card_image']