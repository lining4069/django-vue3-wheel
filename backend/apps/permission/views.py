from rest_framework.decorators import action
from rest_framework.status import HTTP_200_OK

from common.response import SuccessResponse
from common.viewset import BaseModelViewSet
from apps.permission.models import Menu, MenuButton
from service.auth_permission.permission_serializers import (
    MenuSerializer,
    MenuButtonSerializer,
    SampleMenuSerializer
)


# 路由基础操作
class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    route_api_tree_serializer = SampleMenuSerializer

    # 路由接口树
    @action(detail=False, methods=['GET'])
    def menu_tree(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        return SuccessResponse(
            code=HTTP_200_OK,
            message="路由接口树获取成功",
            data=self.route_api_tree_serializer(queryset, many=True).data
        )


class MenuButtonViewSet(BaseModelViewSet):
    queryset = MenuButton.objects.all()
    serializer_class = MenuButtonSerializer
