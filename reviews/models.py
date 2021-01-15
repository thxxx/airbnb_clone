from django.db import models
from core import models as core_models
# Create your models here.


class Review(core_models.TimeStampedModel):

    """ Review Model """
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        # return self.review # 목록에서 보여주는 이름.
        # return self.room.host.username # room으로 들어가서 host로 들어가서 username을 가져올 수 있다. 퍼킹 어썸. 파워 오브 장고 릴레이션싑
        return f'{self.review} - {self.room}'


        