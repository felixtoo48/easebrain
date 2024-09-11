from django.urls import path
from chat.views import ChatRoomAPIView, ChatRoomDetailAPIView, MessageAPIView, MessageDetailAPIView, ForumAPIView, ForumDetailAPIView, ForumCommentAPIView, ForumCommentDetailAPIView



urlpatterns = [
    path('chatrooms/', ChatRoomAPIView.as_view(), name='chatrooms'),
    path('chatrooms/<int:pk>/', ChatRoomDetailAPIView.as_view(), name='chatroom-detail'),
    path('messages/', MessageAPIView.as_view(), name='messages'),
    path('messages/<int:pk>/', MessageDetailAPIView.as_view(), name='message-detail'),
    path('forum-posts/', ForumAPIView.as_view(), name='forum-posts'),
    path('forum-posts/<int:pk>/', ForumDetailAPIView.as_view(), name='forum-post-detail'),
    path('forum/comments/', ForumCommentAPIView.as_view(), name='forum-comments'),
    path('forum/comments/<int:pk>/', ForumCommentDetailAPIView.as_view(), name='forum-comment-detail'),
]