from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'user',
        'count_rooms'
    )

    search_fields = (
        "name", # startswith
    )

    filter_horizontal = ("rooms",) # 보기좋게 해주는 