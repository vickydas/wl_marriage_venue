from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import OR

from .models import Booking
from .serializers import BookingSerializer
from .permissions import IsBookingOwner, IsAdminRole



# Create your views here.

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action in ["create","list"]:
            return [permissions.IsAuthenticated()]
        if self.action in ["confirm","reject"]:
            return [IsAdminRole()]
        if self.action in ["retrieve"]:
            return [ OR (IsBookingOwner(), IsAdminRole())]
        if self.action in ["destroy","update","partial_update"]:
            return [IsBookingOwner()]
        
        return [permissions.IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'SUPERADMIN']:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)
    
    # Admin Actions
    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        booking = self.get_object()
        booking.status = "CONFIRMED"
        booking.save()
        return Response(
            {"message": "Booking confirmed",}
            , status=200)
    
    @action(detail=True, methods=["post"])
    def reject(self, request, pk=None):
        booking = self.get_object()
        booking_status = "REJECTED"
        booking.save()
        return Response({
            "message": "Booking rejected"
        }, status=200)