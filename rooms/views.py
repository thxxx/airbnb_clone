from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
"""
def all_rooms(request): # 장고가 받은 requst를 python object로 변환시켜서 우리한테 준다.
    # 우린 HTTP response를 반환해야돼!!!
    now = datetime.now()
    return HttpResponse(content=f"<h1>hello, {now}</h1>") 
    # render가 리스폰스 안에 html을 넣을 수 있게 해준다.

"""
def all_rooms(request):
    all_rooms = models.Room.objects.all()[:5]
    return render(request, "rooms/home.html", context={
        "rooms": all_rooms
    }) 
    #viwe 이름은 urls.py에 있는 이름과 같아야하고 템플릿 이름은 templates폴더 안에 있는 파일이름이어야 한다.


