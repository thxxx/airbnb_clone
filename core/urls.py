from django.urls import path

from rooms import views as room_views

app_name = "core" # 이건 config.urls의 namespace와 같아야한다.

# urlpatterns는 필수다.
urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"), # 누가 ""경로로 갔을때 room_views의 all_rooms 함수 실행. path는 함수만 실행한다. class 안됨
]