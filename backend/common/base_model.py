# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 1:02 PM
# @Author : lining
# @Remark : 基础类
from django.db import models


class SoftDeleteQuerySet(models.QuerySet):
    pass


class SoftDeleteManager(models.Manager):
    """支持软删除"""

    def __init__(self, *args, **kwargs):
        self.__add_is_del_filter = False
        super(SoftDeleteManager, self).__init__(*args, **kwargs)

    def filter(self, *args, **kwargs):
        # 考虑是否主动传入is_deleted
        if not kwargs.get('is_deleted') is None:
            self.__add_is_del_filter = True
        return super(SoftDeleteManager, self).filter(*args, **kwargs)

    def get_queryset(self):
        if self.__add_is_del_filter:
            return SoftDeleteQuerySet(self.model, using=self._db).exclude(is_deleted=False)
        return SoftDeleteQuerySet(self.model).exclude(is_deleted=True)

    def get_by_natural_key(self, name):
        return SoftDeleteQuerySet(self.model).get(username=name)


class SoftDeleteModel(models.Model):
    """
    软删除模型
    一旦继承,就将开启软删除
    """
    is_deleted = models.BooleanField(null=False, default=False, db_index=True, verbose_name="是否被软删除",
                                     help_text='是否被软删除')
    objects = SoftDeleteManager()

    class Meta:
        abstract = True
        verbose_name = "软删除模型"
        verbose_name_plural = verbose_name

    def delete(self, using=None, soft_delete=True, **kwargs):
        """
        重写删除方法,直接开启软删除
        """
        if soft_delete:
            self.is_deleted = True
            self.save(using=using)
        else:
            super().delete(using=using, **kwargs)


class BaseModel(models.Model):
    """系统建模基类"""
    created_by = models.CharField(max_length=64, null=True, default='admin', verbose_name="创建人")
    updated_by = models.CharField(max_length=64, null=True, default='admin', verbose_name="更新人")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True
        verbose_name = '基础模型'
        verbose_name_plural = verbose_name
