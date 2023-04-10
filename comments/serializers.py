from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "user_id", "content", "created_at"]
        read_only_fields = ["id", "created_at"]

    def create(self, validated_data):
        blog_id = validated_data.pop("blog_id")
        user_id = validated_data.pop("user_id")
        comment = Comment.objects.create(blog_id=blog_id, user_id=user_id, **validated_data)
        return comment
