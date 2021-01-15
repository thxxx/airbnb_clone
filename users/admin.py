from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # 추가
from . import models # from . 은 무슨뜻일까? 같은 폴더 안에있는 model이라는 뜻
# Register your models here.

# admin.site.register(models.User, CustomUserAdmin
# 예전꺼 class CustomUserAdimin(admin.ModelAdmin):
@admin.register(models.User) # decorator는 class 바로 위에 있어야 한다.
class CustomUserAdimin(UserAdmin):
    """ Custom User Admin """
    fieldsets = UserAdmin.fieldsets + ( # 원래 설정 + 원하는거 더하기
        (
            "Custom Profile",
            {
                "fields":(  # 파란 네모
                    #파란네모 안에 들어갈 field
                    "avatar",
                    "gender",
                    "bio", # model에서 저장한 설정 그대로 적용됨
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ), # 
    )
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "language", "currency") # 슈퍼호스트만 보여줄지 아닐지인 filter가 생긴다.

# admin.site.register(models.User, CustomUserAdimin) 데코레이터랑 같은 역할
