# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 1:02 PM
# @Author : lining
# @Remark : 自定义分页类
from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from common.response import SuccessResponse

PAGINATION_DEFAULT_LIMIT = 20
GET_ALL_DATA_KEY = "all"


class BasePagination(PageNumberPagination):
    """
    自定义通用分页处器类
    """
    page_size = PAGINATION_DEFAULT_LIMIT
    page_query_param = 'page'
    page_size_query_param = 'limit'

    def get_page_number(self, request, paginator):
        """
        自定义解析页数
        :param request:
        :param paginator:
        :return:
        """
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        try:
            page_number = int(page_number)
            if page_number < 1:
                raise ValueError()
        except (KeyError, ValueError):
            return 1
        page_number = min(page_number, paginator.num_pages)
        return page_number

    def get_page_size(self, request):
        if self.page_size_query_param:  # 分页类设置分页限制参数
            page_size = request.query_params.get(self.page_size_query_param)
            if not page_size:  # page_size为None，返回默认条数数据
                page_size = self.page_size
            else:
                if page_size == GET_ALL_DATA_KEY:  # page为关键字all,返回全部数据
                    page_size = self.page.paginator.count
                else:  # 传递了page_size_query_param
                    try:
                        page_size = int(page_size)
                        if page_size <= 0:
                            raise ValueError()
                    except (KeyError, ValueError):
                        page_size = self.page_size
            return page_size
        return self.page_size

    def get_paginated_response(self, data):
        message = "获取数据成功"
        data = data
        page = self.page.number
        limit = int(self.get_page_size(self.request))
        total = self.page.paginator.count if self.page else 0
        return SuccessResponse(
            code=HTTP_200_OK,
            message=message,
            data=OrderedDict([
                ("page_data", data),
                ("page", page),
                ("limit", limit),
                ("total", total),
            ]))
