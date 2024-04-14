# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 1:04 PM
# @Author : lining
# @Remark : 相应类
from rest_framework.response import Response
from rest_framework import status


class SuccessResponse(Response):
    def __init__(self, code=status.HTTP_200_OK, message="Successful response", data=None, **kwargs):
        """成功响应初始化函数"""
        response_data = {"code": code, "message": message}
        if data is None:
            data = []
        response_data["data"] = data
        super().__init__(data=response_data, status=status.HTTP_200_OK, **kwargs)


class ErrorResponse(Response):
    def __init__(self, code=status.HTTP_400_BAD_REQUEST, message="Failed requests", data=None, **kwargs):
        """失败响应初始化函数"""
        response_data = {"code": code, "message": message, "data": data}
        super().__init__(data=response_data, status=status.HTTP_400_BAD_REQUEST, **kwargs)
