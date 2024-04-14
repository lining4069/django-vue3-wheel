from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from django.contrib.auth import authenticate

from common.response import SuccessResponse


class LoginView(APIView):
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
