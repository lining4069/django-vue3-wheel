# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/16 9:50 AM
# @Author : lining
# @Remark :
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.permission.views import (
    MenuViewSet,
    MenuButtonViewSet
)

router = DefaultRouter()
router.register('menu', MenuViewSet, basename='menu')
router.register('menu_button', MenuButtonViewSet, basename='menu_button')

urlpatterns = [
    path('', include(router.urls)),
]
