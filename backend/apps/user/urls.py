# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 9:07 PM
# @Author : lining
# @Remark :
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)

from apps.user.views import (
    LoginView
)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
