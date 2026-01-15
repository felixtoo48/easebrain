from django.urls import reverse
from chat.models import ChatRoom, Message, ForumPost, ForumComment
from easebrain.models import User

from rest_framework.test import APITestCase

class ChatViewsTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="janedoe@gmail.com",
            password="1234",
            name="Jane Doe"
        )
        self.chatrooms_url = reverse("chatrooms")
        return super().setUp()
    
    def test_chatroom_creation(self):
        room_data = {
            "name": "Test Chat Room",
            "description": "This is a test chat room.",
        }

        response = self.client.post(self.chatrooms_url, room_data, format="json")
        self.assertEqual(response.status_code, 201)

    def test_message_creation(self):
        chatroom = ChatRoom.objects.create(
            name="Test Chat Room",
            description="This is a test chat room.",
        )

        message_data = {
            "user": self.user.id,
            "chatroom": chatroom.id,
            "content": "This is a test message.",
        }

        response = self.client.post(reverse("messages"), message_data, format="json")
        self.assertEqual(response.status_code, 201)

    
    def test_forum_post_creation(self):
        forum_post_data = {
            "user": self.user.id,
            "content": "This is a test forum post.",
        }

        response = self.client.post(reverse("forum-posts"), forum_post_data, format="json")
        self.assertEqual(response.status_code, 201)


    def test_forum_comment_creation(self):
        forum_post = ForumPost.objects.create(
            user=self.user,
            content="This is a test forum post.",
        )

        forum_comment_data = {
            "user": self.user.id,
            "post": forum_post.id,
            "content": "This is a test forum comment.",
        }

        response = self.client.post(reverse("forum-comments"), forum_comment_data, format="json")
        self.assertEqual(response.status_code, 201)