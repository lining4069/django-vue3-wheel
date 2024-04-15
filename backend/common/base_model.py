# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 1:02 PM
# @Author : lining
# @Remark : 基础类
from django.db import models


class SoftDeleteManager(models.Manager):
    """支持软删除的管理器"""

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def all(self):
        """
        返回包括被软删除的所有对象
        """
        return super().get_queryset()

    def only_deleted(self):
        """
        获取被软删除的数据
        :return:
        """
        return super().get_queryset().filter(is_deleted=True)


class SoftDeleteModel(models.Model):
    """
    软删除模型
    一旦继承,就将开启软删除
    """
    is_deleted = models.BooleanField(verbose_name="是否被软删除", default=False, help_text='是否被软删除')
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

    def hard_delete(self, using=None, **kwargs):
        """
        执行硬删除
        """
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
