from rest_framework import serializers
from chat.models import ChatRoom, Message, ForumPost, ForumComment

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumPost
        fields = "__all__"


class ForumCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComment
        fields = "__all__"