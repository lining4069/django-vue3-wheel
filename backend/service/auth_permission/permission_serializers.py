# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/15 11:18 PM
# @Author : lining
# @Remark : 权限管理序列化 角色授权，角色绑定用户或用户组
from rest_framework.serializers import SerializerMethodField, ModelSerializer

from apps.permission.models import Menu, MenuButton
from apps.role.models import Role, RoleMenuPermission, RoleMenuButtonPermission
from common.serializer import BaseModelSerializer
from service.auth_permission.serializers import SampleUserSerializer, SampleGroupSerializer


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


# 用于生成路由接口树的sample接口序列化和路由序列化
class ReadOnlySampleMenuButtonSerializer(ModelSerializer):
    class Meta:
        model = MenuButton
        fields = ['id', 'name']


# 路由接口树和带权路由接口树
class ReadOnlySampleMenuSerializer(ModelSerializer):
    children = SerializerMethodField(method_name='get_children', read_only=True)  # 自路由
    buttons = ReadOnlySampleMenuButtonSerializer(many=True, read_only=True)  # 当前路由下的接口列表

    def get_children(self, obj: Menu):
        child_menu_queryset = Menu.objects.filter(parent_id=obj.id)
        return ReadOnlySampleMenuSerializer(child_menu_queryset, many=True).data

    class Meta:
        model = Menu
        fields = ['id', 'name', 'buttons', 'children']


# 角色绑定组织关系序列化
class ReadOnlyRoleORSerializer(ModelSerializer):
    role_groups = SampleGroupSerializer(many=True, read_only=True)  # 角色绑定给了哪些组
    role_users = SampleUserSerializer(many=True, read_only=True)  # 角色绑定了哪些用户

    class Meta:
        model = Role
        fields = ['id', 'name', 'is_active', 'role_groups', 'role_users']


# 菜单/路由权限管理
class MenuPermissionManageSerializer(ModelSerializer):
    # 获取带权(是否具备该接口权限)路由接口树
    @classmethod
    def get_route_api_tree_by_role_id(cls, role_id: int):
        """
        根据角色id获取路由权限树
        :param role_id:角色id
        :return:
        """
        tree_with_checked = []
        # 根据角色列表获取由这些角色解析出的路由id和接口id
        checked_menu_ids = []
        checked_button_id_info = {}

        # 处理角色授权过的路由和接口
        role_menu_queryset = RoleMenuPermission.objects.filter(role_id=role_id)
        if role_menu_queryset.exists:
            checked_menu_ids.extend([getattr(_, 'menu_id') for _ in role_menu_queryset])
        role_button_queryset = RoleMenuButtonPermission.objects.filter(role_id=role_id)
        if role_button_queryset.exists:
            checked_button_id_info.update(
                {getattr(_, "menu_button_id"): getattr(_, "data_range", 0) for _ in role_button_queryset if getattr(_, "menu_button_id")}
            )

        # 构建带 标识的路由接口树
        menu_queryset = Menu.objects.all().order_by('sort').select_related('parent')
        menu_button_queryset = MenuButton.objects.all()

        for menu_ins in menu_queryset:
            # 处理菜单节点信息
            menu_node = {
                'id': menu_ins.id,
                'name': menu_ins.name,
                'buttons': [],
                'children': []
            }
            # 处理节点是否被授权给角色
            if menu_ins.id in checked_menu_ids:
                menu_node.update({"is_checked": True})
            else:
                menu_node.update({"is_checked": False})
            # 处理菜单内的接口
            for button_ins in menu_button_queryset:
                if button_ins.menu_id == menu_ins.id:
                    # 处理页面内基础接口基础信息
                    button_node = {
                        'id': button_ins.id,
                        'name': button_ins.name
                    }
                    # 处理接口授权状态
                    if button_ins.id in checked_button_id_info.keys():
                        button_node.update({"is_checked": True})
                    else:
                        button_node.update({"is_checked": False})
                    menu_node["buttons"].append(button_node)
            if not menu_ins.parent:
                tree_with_checked.append(menu_node)
            else:
                try:
                    parent_menu = next(m for m in tree_with_checked if m['id'] == menu_ins.parent_id)
                    parent_menu['children'].append(menu_node)
                except StopIteration:
                    # 如果没有找到父级菜单，则忽略此菜单节点
                    pass
        return tree_with_checked

    @classmethod
    def get_organization_relationship_by_role_id(cls, role_id) -> dict:
        """
        根据角色id获取其绑定过的组织关系
        :param role_id: 角色id
        :return:
        """
        role_ins = Role.objects.filter(id=role_id).first()
        if role_ins:
            return ReadOnlyRoleORSerializer(role_ins, many=False).data
        else:
            return {}

    class Meta:
        model = RoleMenuPermission
        fields = '__all__'


# 接口权限管理
class ButtonPermissionManageSerializer(ModelSerializer):
    class Meta:
        model = RoleMenuButtonPermission
        fields = '__all__'
