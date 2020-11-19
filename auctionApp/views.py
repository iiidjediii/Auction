from auctionApp.models import Auction
from auctionApp.serializers import AuctionSerializer, UserSerializer

from rest_framework import generics

from django.contrib.auth.models import User

from rest_framework import permissions
from .permissions import IsLotAuthorOrReadOnly
"""
    views as classes
"""


class AuctionList(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(lot_author=self.request.user)


class AuctionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsLotAuthorOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""
    views as functions
"""
# from rest_framework import status
#
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# @api_view(['GET', 'POST'])
# def auction_list(request, format=None):
#     """
#     List all auctions, or create a new auction.
#     """
#     if request.method == 'GET':
#         auctions = Auction.objects.all()
#         serializer = AuctionSerializer(auctions, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = AuctionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'POST'])
# def auction_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete auction.
#     """
#     try:
#         auction = Auction.objects.get(pk=pk)
#     except Auction.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = AuctionSerializer(auction)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#
#         serializer = AuctionSerializer(auction, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         auction.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
