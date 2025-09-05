from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from api.models import Listing
from api.serializers import ListingSerializer
from rest_framework import filters
from api.filters import GuelphFilter


# Create your views here.
class ListingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_class = GuelphFilter
    #filterset_fields = ('price', 'date_posted', 'bedroom_count', 'bathroom_count', 'utilities')
    #filter_backends = []