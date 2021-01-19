from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    # 위의 register에 적힌 것들에 연결된다
    list_display = (
        "name",
        "used_by"
    )

    def used_by(self, obj):
        return obj.rooms.count()
    


@admin.register(models.Room)  # admin pannel과 연결!
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (  # all over the place인것들 정리
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",), # 접을 수 있는 섹션. collapsable한. 을 만들어준다
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "check_out", # 여기에 many to many는 못넣는다. 그래서 함수를 만들어줄 필요가있다
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    def count_amenities(self, obj): # self는 roomadmin, obj는 현재 row
# 장고모델과 relationships가 어떻게 작동하는지 보자
        # print(obj.amenities.all()) # <QuertSet [<Amenity: Shower>] 라고 뜨는데 중요한 기능이다.
        return obj.amenities.count() # count 갯수!

    def count_photos(self, obj):  
        return obj.photos.count()

    ordering = ('name', 'price') # 정렬 순서. 1순위, 2순위 물론 직접 눌러서도 정렬 가능하고

    list_filter = (
        "instant_book",
        "host__superhost",  # host안의 슈퍼호스트
        "price",
        "room_type",
        "amenities",
        "facilities",
        "city",
    )
    # select room 페이지에서 보일것들
    # https://docs.djangoproject.com/en/3.1/ref/contrib/admin/ 여기서 확인 가능
    search_fields = ["city", "host__username"]  # 여기서는 __로 포린키처럼 사용
    # none이면 대소문자 고려x ^붙이면 startswith, =는 대소문자 고려

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    pass
