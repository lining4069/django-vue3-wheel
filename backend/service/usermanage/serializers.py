# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 8:36 PM
# @Author : lining
# @Remark : 用户、组、角色 序列化
from rest_framework import serializers

from apps.user.models import User
from common.serializer import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
