from django.db import models
from django.conf import settings


from core.models import AbstractBaseModel


# Create your models here.
class ChatRoom(AbstractBaseModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='userchatrooms')
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chatrooms', null=True)

    def __str__(self):
        return self.name
    

class Message(AbstractBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}: {self.content[:30]}"


class ForumPost(AbstractBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forum_posts')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}: {self.content[:30]}"
    

class ForumComment(AbstractBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='forum_comments')
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name}: {self.content[:30]}"