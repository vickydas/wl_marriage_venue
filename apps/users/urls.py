from django.urls import path
from .views import MeView, UpdateProfileView, UploadProfilePictureView

urlpatterns = [
    path('me/', MeView.as_view(), name="me"),
    path("update-profile/", UpdateProfileView.as_view()),
    path("upload_image", UploadProfilePictureView.as_view())
]