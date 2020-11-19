from rest_framework import serializers
from auctionApp.models import Auction
from django.contrib.auth.models import User



class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id', 'lot_title', 'lot_description', 'lot_start_price', 'lot_end_date', 'lot_last_bet_price']

        lot_author = serializers.ReadOnlyField(source='lot_author.username')


class UserSerializer(serializers.ModelSerializer):
    auctions = serializers.PrimaryKeyRelatedField(many=True, queryset=Auction.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'auctions']
