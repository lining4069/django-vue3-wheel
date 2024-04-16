# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/15 11:18 PM
# @Author : lining
# @Remark : 权限管理序列化 角色授权，角色绑定用户或用户组
from apps.permission.models import Menu, MenuButton

from common.serializer import BaseModelSerializer


# 接口序列化
class MenuButtonSerializer(BaseModelSerializer):
    class Meta:
        model = MenuButton
        fields = '__all__'


# 路由序列化
class MenuSerializer(BaseModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        depth = 1
# 接口管理
# 系统 路由接口树
# 角色授权和角色 路由接口树
# 角色绑定用户、角色绑定用户
