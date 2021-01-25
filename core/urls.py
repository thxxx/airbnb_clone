from django.urls import path

from rooms import views as room_views

# urlpatterns는 필수다.
urlpatterns = [
    path("", room_views.all_rooms), # 누가 ""경로로 갔을때 room_views의 all_rooms 함수 실행
]