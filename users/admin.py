from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # 추가
from . import models # from . 은 무슨뜻일까? 같은 폴더 안에있는 model이라는 뜻
# Register your models here.

# admin.site.register(models.User, CustomUserAdmin
@admin.register(models.User) # decorator는 class 바로 위에 있어야 한다.
# 예전꺼 class CustomUserAdim(admin.ModelAdmin):
class CustomUserAdim(UserAdmin):
    """ Custom User Admin """
    fieldstes = (
        (
            "Banana",
            {
                "fileds"
            }
        )
    )
    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = ("superhost", "language", "currency") # 슈퍼호스트만 보여줄지 아닐지인 filter가 생긴다.

