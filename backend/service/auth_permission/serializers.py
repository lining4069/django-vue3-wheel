# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 8:36 PM
# @Author : lining
# @Remark : 用户、组、角色 序列化
from rest_framework import serializers

from apps.permission.models import Menu, MenuButton
from apps.role.models import Role, RoleMenuPermission, RoleMenuButtonPermission
from apps.group.models import Group
from apps.user.models import User
from common.serializer import BaseModelSerializer


# 菜单按钮/api序列化
class MenuButtonSerializer(BaseModelSerializer):
    class Meta:
        model = MenuButton
        fields = '__all__'
        read_only_fields = ['id']


# 系统菜单序列化
class MenuSerializer(BaseModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


# 角色序列化
class RoleSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


# 组序列化
class GroupSerializer(BaseModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ['id']
        depth = 1


# 用户序列化
class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 1
