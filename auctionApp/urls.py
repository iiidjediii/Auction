from django.urls import path
from auctionApp import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "auctionApp"

urlpatterns = [
    path('auctionApp/', views.AuctionList.as_view()),
    path('auctionApp/<int:pk>/', views.AuctionDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)