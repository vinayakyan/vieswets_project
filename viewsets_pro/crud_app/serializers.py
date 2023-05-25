from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def validate_content(self, value):
        if not len(value) >= 50:
            raise serializers.ValidationError("Post content should have atleast 50 characters")
        return value