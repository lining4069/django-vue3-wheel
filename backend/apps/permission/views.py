from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from common.response import SuccessResponse, ErrorResponse
from common.viewset import BaseModelViewSet
from apps.permission.models import Menu, MenuButton
from apps.role.models import RoleMenuPermission, RoleMenuButtonPermission
from service.auth_permission.permission_serializers import (
    MenuSerializer,
    MenuButtonSerializer,
    ReadOnlySampleMenuSerializer,
    MenuPermissionManageSerializer,
    ButtonPermissionManageSerializer
)


# 菜单/路由视图
class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    # 路由接口树
    @action(detail=False, methods=['GET'])
    def menu_tree(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return SuccessResponse(
            code=HTTP_200_OK,
            message="路由接口树获取成功",
            data=ReadOnlySampleMenuSerializer(queryset, many=True).data
        )

    # 带权路由接口树


# 接口管理-基础操作视图
class MenuButtonViewSet(BaseModelViewSet):
    queryset = MenuButton.objects.all()
    serializer_class = MenuButtonSerializer


# 路由权限管理视图
class MenuManageViewSet(BaseModelViewSet):
    queryset = RoleMenuPermission.objects.all()
    serializer_class = MenuPermissionManageSerializer

    @action(methods=["POST"], detail=False)
    def role_checked(self, request, *args, **kwargs):
        role_id = request.data.get("role_id")
        if role_id is None:
            return ErrorResponse(
                code=HTTP_400_BAD_REQUEST,
                message="请传递要获取路由接口树的角色id",
                data=[]
            )
        tree_with_checked = MenuPermissionManageSerializer.get_route_api_tree_by_role_id(role_id=role_id)
        return SuccessResponse(
            code=HTTP_200_OK,
            message="获取角色带权路由接口树正常",
            data=tree_with_checked
        )

    # 获取角色当前绑定用户组和用户状态
    @action(methods=["POST"], detail=False)
    def role_relation(self, request, *args, **kwargs):
        role_id = request.data.get("role_id")
        if role_id is None:
            return ErrorResponse(
                code=HTTP_400_BAD_REQUEST,
                message="请传递要获取绑定的角色id",
                data=[]
            )
        role_relationship_state = MenuPermissionManageSerializer.get_organization_relationship_by_role_id(role_id=role_id)
        return SuccessResponse(
            code=HTTP_200_OK,
            message="获取角色绑定关系状态正常",
            data=role_relationship_state
        )


# 接口权限管理视图
class ButtonManageViewSet(BaseModelViewSet):
    queryset = RoleMenuButtonPermission.objects.all()
    serializer_class = ButtonPermissionManageSerializer
