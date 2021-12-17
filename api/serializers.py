from rest_framework import serializers
from api.models import YoutubeAPIResult


# Youtube model serializer is for serializing the database model
class YoutubeResultAPIModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeAPIResult
        fields = "__all__"
