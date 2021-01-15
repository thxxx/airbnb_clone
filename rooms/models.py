from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models # 모델간의 연결..!
# Create your models here.

class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Items """

    name = models.CharField(max_length=80)

    class Meta:
        abstract=True
    
    def __str__(self):
        return self.name


class RoomType(AbstractItem): # 다 공유하는 속성이어서 이걸로 서치하고싶은거면 이렇게 만드나?
    """ RoomType Object """

    class Meta:
        verbose_name_plural = "Room Type"
        ordering = ['created'] # core파일 타임스탬프 안에 있는. name도 가능


class Amenity(AbstractItem):

    """ Amenity """
    class Meta:
        verbose_name_plural = "Amenities" # 이게 없으면 Amenitys

class Facility(AbstractItem):

    """ Facility """
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ Houserule model definition """
    class Meta:
        verbose_name_plural = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo model """
    caption = models.CharField(max_length=80)
    ifile = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE) # Room에 스트링 처리를 하면 해당 class가 Photo뒤에 생성되었더라도 에러 x

    def __str__(self): # Str 메소드 정의
        return self.caption



class Room(core_models.TimeStampedModel):
    # room의 디테일로 넣어줄 것들 생성

    # 패키지
    # pipenv install django-countries
    # 세팅의 써드파티앱에 장고컨트리스 추가

    name = models.CharField(max_length=140) # null=True가 없으면 필수사항
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField() # date말고 시간.
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
 
    host = models.ForeignKey("users.User", on_delete=models.CASCADE) # User model과 연결해야 한다. foreignKey 이건 임포트가 필요함.
    # on_delete는 삭제 되었을때의 행동. CASCADE는 이 유저가 생성한 Room도 지워진다는 뜻. https://docs.djangoproject.com/en/3.1/
    # on_delete에 들어갈 수 있는건 많다. PROTECT는 룸을 지우기전까진 유저를 지울수 없다.

    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True) # room은 host를 가지지만 user는 roonm을 가지지 않는다.
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities =  models.ManyToManyField(Facility, blank=True)
    house_rules =  models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name