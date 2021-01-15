from django.db import models

# Create your models here.

class TimeStampedModel(models.Model): # 이건 User빼고 다른데서 다 쓰일거야

    created = models.DateTimeField(auto_now_add=True) #필드가 모델을 save할 대 date 랑 time을 기록 장고가 내가 세로운 model을 만들면 생성 날짜랑 시간을 여기 넣어주게한다.
    updated = models.DateTimeField(auto_now=True) # 새로운 날짜로 업데이트 해준다.

    class Meta:
        abstract = True # abstract 모델은 모델이지만 db에 나타나지 않는다. 확장할때 사용.


    
