# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 8:36 PM
# @Author : lining
# @Remark : 用户、组、角色 序列化 组织关系层面上的逻辑处理
from collections import OrderedDict
from rest_framework.serializers import SerializerMethodField
from django.conf import settings

from apps.role.models import Role
from apps.group.models import Group
from apps.user.models import User
from common.serializer import BaseModelSerializer


# 简单信息角色序列化
class SampleRoleSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


# 简单用户组序列化
class SampleGroupSerializer(BaseModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


# 简单信息用户序列化
class SampleUserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'display_name']


# 角色序列化
class RoleSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ['id', 'is_deleted']


# 组序列化
class GroupSerializer(BaseModelSerializer):
    roles = SampleRoleSerializer(many=True, read_only=True)  # 组具有哪些角色
    group_users = SampleUserSerializer(many=True, read_only=True)  # 组下面具有哪些用户

    def validate(self, attrs):
        roles = attrs.get("roles", [])
        if not bool(roles):
            attrs["roles"] = [settings.DEFAULT_ROLE_ID]
        return attrs

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ['id', 'is_deleted']


# 用户序列化
class UserSerializer(BaseModelSerializer):
    roles = SampleRoleSerializer(many=True, read_only=True)  # 用户具有哪些角色
    groups = SampleGroupSerializer(many=True, read_only=True)  # 用户处于哪些组
    roles_all = SerializerMethodField(method_name="get_roles_by_groups_roles", read_only=True)  # 用户因为组而获得的角色

    def validate(self, attrs):
        roles = attrs.get("roles", [])
        if not roles:
            attrs["roles"] = [settings.DEFAULT_ROLE_ID]
        groups = attrs.get("groups", [])
        if not groups:
            attrs["groups"] = [settings.DEFAULT_GROUP_ID]
        return attrs

    def get_roles_by_groups_roles(self, obj):
        roles_all = []
        for group in obj.groups.all():
            group_roles_serializer = SampleRoleSerializer(group.roles, many=True)
            roles_all.extend(group_roles_serializer.data)
        roles_by_role_serializer = SampleRoleSerializer(obj.roles.all(), many=True)
        roles_all.extend(roles_by_role_serializer.data)
        # roles_all 去重
        unique_list = list(OrderedDict((d['id'], d) for d in roles_all).values())

        return unique_list

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'is_deleted']
        extra_kwargs = {
            'password': {'write_only': True}
        }
