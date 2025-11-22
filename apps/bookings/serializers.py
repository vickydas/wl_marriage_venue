from rest_framework import serializers
from .models import Booking
from apps.venues.models import Venue
from datetime import date

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    venue_name = serializers.CharField(source="venue.name", read_only=True)
    user_email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Booking
        fields = [
            'id',
            'user',
            'user_email',
            'venue',
            'venue_name',
            'from_date',
            'to_date',
            'purpose',
            'payment_proof',
            'status',
            'created_at',
        ]
        read_only_fields = ['status', 'created_at']

    def validate(self, data):
        from_date = data.get("from_date")
        to_date = data.get("to_date")
        venue = data.get("venue")

        if from_date > to_date:
            raise serializers.ValidationError("from_date must be before to_date.")
        
        # Check for overlapping bookings
        overlaps = Booking.objects.filter(
            venue=venue,
            status="CONFIRMED",
            from_date__lte=to_date,
            to_date__gte=from_date
        )

        if overlaps.exists():
            raise serializers.ValidationError("The venue is already booked for the selected dates.")
        
        return data
    
    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
    
