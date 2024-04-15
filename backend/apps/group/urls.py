# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/15 6:37 PM
# @Author : lining
# @Remark :
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.group.views import (
    GroupViewSet
)

router = DefaultRouter()
router.register(r'group', GroupViewSet, basename='group')

urlpatterns = [
    path('', include(router.urls)),
]
