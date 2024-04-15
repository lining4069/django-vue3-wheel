# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/15 3:49 PM
# @Author : lining
# @Remark :
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.role.views import RoleViewSet

router = DefaultRouter()
router.register(r'role', RoleViewSet, basename='role')

urlpatterns = [
    path('', include(router.urls)),
]
