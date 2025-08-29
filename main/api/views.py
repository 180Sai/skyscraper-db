from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from api.models import Listing
from api.serializers import ListingSerializer

# Create your views here.
class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    filter_backends = [
    ]