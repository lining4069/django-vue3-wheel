from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from django.contrib.auth import authenticate

from apps.user.models import User
from common.response import SuccessResponse
from service.auth_permission.serializers import UserSerializer
from common.viewset import BaseModelViewSet


# 登陆视图
class LoginView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    # 登陆接口
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return SuccessResponse(
                code=status.HTTP_200_OK,
                message="登录成功",
                data={"refresh": str(refresh), "token": str(refresh.access_token)}
            )
        return SuccessResponse(code=status.HTTP_401_UNAUTHORIZED, message="登录失败", data=[])


# 用户基础操作视图
class UserViewSet(BaseModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
