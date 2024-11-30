from rest_framework import serializers
from .models import UserEmployeur, Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']


class UserEmployeurSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True) 
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(), source='post', write_only=True, required=False
    ) 
    class Meta:
        model = UserEmployeur
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'post',
            'post_id',
        ]
