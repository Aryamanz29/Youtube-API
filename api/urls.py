from django.urls import path
from api.views import get_youtubeapi_details

urlpatterns = [
    path("api/youtube/", get_youtubeapi_details.as_view(), name="Youtube API Results"),
]
