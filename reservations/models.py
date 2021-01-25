from django.db import models
from django.utils import timezone
from core import models as core_models
# Create your models here.


class Reservation(core_models.TimeStampedModel):
    """ Reservation Model """

    STATUS_PENDONG = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDONG, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED,  "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDONG)

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)

    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.room} - {self.check_in}'

    
    def in_progress(self): # 시간사이 인지를 구분해서 예전 예약인지 아닌지 표시
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out
    in_progress.boolean = True # x 표시 v 표시

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out
    is_finished.boolean = True

    