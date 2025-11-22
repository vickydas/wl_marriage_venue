from rest_framework import serializers
from .models import Venue, Utility


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ['id','name','is_available']

class VenueSerializer(serializers.ModelSerializer):
    utilities = UtilitySerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Venue
        fields = "__all__"

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
