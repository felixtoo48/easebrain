from django.test import TestCase

from easebrain.models import User
from chat.models import ChatRoom, Message, ForumPost, ForumComment


class TestChatModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="janedoe@gmail.com",
            password="1234",
            name="Jane Doe"
        )
    def test_chatroom_creation(self):
        chatroom = ChatRoom.objects.create(
            name="Test Chat Room",
            description="This is a test chat room.",
        )
        chatroom.participants.set([])
        chatroom.save()

        self.assertIsInstance(chatroom, ChatRoom)
        self.assertEqual(str(chatroom), "Test Chat Room")
        self.assertIsInstance(chatroom.name, str)
        self.assertIsInstance(chatroom.description, str)

    def test_message_creation(self):
        chatroom = ChatRoom.objects.create(
            name="Test Chat Room",
            description="This is a test chat room.",
        )
        message = Message.objects.create(
            user=self.user,
            chatroom=chatroom,
            content="This is a test message.",
        )

        self.assertIsInstance(message, Message)
        self.assertEqual(str(message), "Jane Doe: This is a test message.")


    def test_forum_post_creation(self):
        forum_post = ForumPost.objects.create(
            user=self.user,
            content="This is a test forum post.",
        )

        self.assertIsInstance(forum_post, ForumPost)
        self.assertEqual(
            str(forum_post), "Jane Doe: This is a test forum post."
        )          

    def test_forum_comment_creation(self):
        forum_post = ForumPost.objects.create(  
            user=self.user,
            content="This is a test forum post.",
        )

        forum_comment = ForumComment.objects.create(
            user=self.user,
            post=forum_post,
            content="This is a test forum comment.",
        )

        self.assertIsInstance(forum_comment, ForumComment)
        self.assertEqual(
            str(forum_comment), "Jane Doe: This is a test forum comment."
        )