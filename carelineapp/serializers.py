from rest_framework import serializers, fields
from . import models


class TopicSerializer(serializers.ModelSerializer):
    counselling_topic = fields.URLField(source='counselling_topic.file.url')

    class Meta:
        model = models.Topic
        fields = ('id', 'title', 'introduction', 'counselling_topic', 'custom_url', )

