from apps.group.models import Group
from common.viewset import BaseModelViewSet
from service.auth_permission.serializers import GroupSerializer


# 组基础操作视图
class GroupViewSet(BaseModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
