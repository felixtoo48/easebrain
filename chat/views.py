from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, status

from chat.models import ChatRoom, Message, ForumPost, ForumComment
from chat.serializers import ChatRoomSerializer, MessageSerializer, ForumPostSerializer, ForumCommentSerializer
# Create your views here.
class ChatRoomAPIView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class ChatRoomDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    lookup_field = "pk"
    


class MessageAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    lookup_field = "pk"


class ForumAPIView(generics.ListCreateAPIView):
    queryset = ForumPost.objects.all().order_by("-created")
    serializer_class = ForumPostSerializer


class ForumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all().order_by("-created")
    serializer_class = ForumPostSerializer

    lookup_field = "pk"


class ForumCommentAPIView(generics.ListCreateAPIView):
    queryset = ForumComment.objects.all().order_by("-created")
    serializer_class = ForumCommentSerializer


class ForumCommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumComment.objects.all().order_by("-created")
    serializer_class = ForumCommentSerializer

    lookup_field = "pk"