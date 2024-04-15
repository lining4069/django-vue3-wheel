from apps.role.models import Role
from common.viewset import BaseModelViewSet
from service.auth_permission.serializers import RoleSerializer


class RoleViewSet(BaseModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
