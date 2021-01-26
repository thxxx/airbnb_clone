from django.shortcuts import render
from django.http import HttpResponse
from . import models
import math

# Create your views here.
"""
def all_rooms(request): # 장고가 받은 requst를 python object로 변환시켜서 우리한테 준다.
    # 우린 HTTP response를 반환해야돼!!!
    now = datetime.now()
    return HttpResponse(content=f"<h1>hello, {now}</h1>") 
    # render가 리스폰스 안에 html을 넣을 수 있게 해준다.

"""
# url에서 오는 모든 것은 get request야.
# &page=2%citiy=seoul print(request.GET) 하면 queryDict: {'page': ['2'], 'city':['seoul']} 출력해준다.

def all_rooms(request):
    page = request.GET.get("page", 1) # default에서는 1을 갖는다는 뜻.
    page = int(page or 1)
    page_size = 10
    limit = page_size*page
    all_rooms = models.Room.objects.all()[limit-page_size : limit] # [offset:limit] sql에서 제한을한다. 쿼리를 슬라이싱하면 새로운 쿼리를 반환한다.
    page_count = models.Room.objects.count()/page_size 
    return render(request, "rooms/home.html", context={ # 이걸로 값을 전달!!
        "rooms": all_rooms,
        "page":page,
        "page_count": math.ceil(page_count),
        "page_range": range(1, math.ceil(page_count)+1),
    }) 
    #viwe 이름은 urls.py에 있는 이름과 같아야하고 템플릿 이름은 templates폴더 안에 있는 파일이름이어야 한다.


