from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# 데이터가 보여지는 방법
# User는 이미 만들어진게 어느 정도 있으니까 다른 app과 다른 코드를 취한다.

# AbstractUser가 뭔지를 알기위해 코드를 뜯어보면 좋다.


class User(AbstractUser):
    """ Explanation """
    # 자기소개, 성별 등 원하는 속성을 추가
    # 여기에 뭘 쓰든 장고가 알아서 form으로 만들어주고 마이그레이션과 함께
    # 데이터베이스에다가 form에 필요한 정보를 요청할거야.

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
#charfield이 커스터마이징
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    ) # 이건 단지 폼이기때문에 데이터베이스에 변화를 일으키진 않는다 
      # -> 마이그레이션 노 필요.

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"), # ( 데이터베이스로 갈 값, FORM에 보여질 값)
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    )

    # 필드를 추가한다. 필드는 장고 documentation에서 뭐가 있는지 볼 수 있음
    bio = models.TextField(default="")
    # ㅇ아직 데이터베이스가 bio에 대한 정보가 없다.
    # -> 마이그레이션 해줘야한다. 마이그레이션 생성, migrate
    # -> add user에서 bio필드 확인 가능!

    # default를 써야하는 이유는 원래 존재하던 user에도 어떤 값을 줘야하니까
    avatar = models.ImageField(null=True, blank=True)  # pillow install해야 사용 가능.
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10, 
        null=True, blank=True,
        ) # 비어있어도 상관없다.
    
    # Datetime과 Date 필드가 있다.
    birthdate = models.DateField(null=True)
    language = models.CharField(
        null=True, blank=True,
        choices = LANGUAGE_CHOICES,
        max_length=2,
    )
    currency = models.CharField(
        null=True, blank=True,
        choices = CURRENCY_CHOICES,
        max_length=3,
    )
    superhost = models.BooleanField(default = False)


    pass  # 이 모델을 adimg에 연결해야한다.. 왜?
