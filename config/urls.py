"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # 파일을 직접이 아니라 다른 경로로 수입한다.
from django.conf.urls.static import static


urlpatterns = [
    path("", include("core.urls", namespace="core")), # ""의 경로를 인식하면 core.urls로 가서 살펴보고 없으면 다시 뒤의 path로 간다.
    path('admin/', admin.site.urls), #adimin페이지로 가는 url. 장고가 uRL.PY를 실행한다.
    # url, view다. view는 내가 이 요청에 반응하는 방법.
]

#프로덕션인지 개발중인지를 감지해서 error page 보여주는게 DEBUG = True

if settings.DEBUG: # 고로 이건 개발자 모드일때만. 이렇게 안하면 수많은 사용자를 가지게되면 코드서버에서 더 많은 디스크 공간을 소비하게된다
    # 나중에 어떻게 아마콘ㅍ ㅏ일을 제공하는지 한다
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    # media_url으로 접근하면 사용자에게는 그 path를 보여주되, document_root 으로 가서 파일을 찾아라
