from rest_framework import generics

from . import models
from . import serializers

from rest_framework.reverse import reverse
from rest_framework.views import APIView

class TopicListView(generics.ListAPIView):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer

