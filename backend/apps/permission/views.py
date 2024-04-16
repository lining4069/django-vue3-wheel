from apps.permission.models import Menu, MenuButton
from common.viewset import BaseModelViewSet
from service.auth_permission.permission_serializers import MenuSerializer, MenuButtonSerializer


# 路由基础操作
class MenuViewSet(BaseModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuButtonViewSet(BaseModelViewSet):
    queryset = MenuButton.objects.all()
    serializer_class = MenuButtonSerializer
