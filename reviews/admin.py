from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'rating_average') # str 이랑 model의 methond를 쓸 수 있다.