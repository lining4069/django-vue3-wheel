from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions, viewsets
from django.contrib.auth import authenticate

from apps.user.models import User
from common.response import SuccessResponse
from service.usermanage.serializers import UserSerializer
from common.pagination import PageNumberPagination


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return SuccessResponse(
            code=status.HTTP_200_OK,
            data=serializer.data,
            message="用户列表获取成功"
        )
