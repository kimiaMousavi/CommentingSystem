from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('author', 'text', 'pk', 'date')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post_id',)
