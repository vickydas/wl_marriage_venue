from django.shortcuts import render
from .models import Venue
from .serializers import VenueSerializer
from .permissions import IsAdminUserRole
from rest_framework import viewsets, permissions
# Create your views here.

from rest_framework.parsers import MultiPartParser, FormParser

class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUserRole()]
        return [permissions.AllowAny()]
