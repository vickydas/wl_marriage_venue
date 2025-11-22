from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer


# Create your views here.
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data)
    
class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        user.contact_number = request.data.get('contact_number', user.contact_number)
        user.save()
        return Response({"message": "Profile updated"})

class UploadProfilePictureView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        file = request.FILES.get('profile_image')
        if file:
            user.profile_image = file
            user.save()
            return Response({"message": "Profile image uploaded"})
        return Response({"error": "No file provided"}, status=400)