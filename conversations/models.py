from django.db import models
from core import models as core_models

# Create your models here.

class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField("users.User", blank=True)

#    user = models.ForeignKey("users.User", on_delte)

    def __str__(self):
        return str(self.created) # str아니면 오류난다.


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} says: {self.text}'
