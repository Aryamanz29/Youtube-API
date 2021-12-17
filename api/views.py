from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from api.models import YoutubeAPIResult
from api.serializers import YoutubeResultAPIModelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

class get_youtubeapi_details(generics.ListAPIView):
    queryset = YoutubeAPIResult.objects.order_by("-publish_datetime")
    serializer_class = YoutubeResultAPIModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["video_title", "publish_datetime"]
    pagination_class = StandardResultsSetPagination
