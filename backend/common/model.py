# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 1:02 PM
# @Author : lining
# @Remark : 基础类
import uuid

from django.db import models


class SoftDeleteManager(models.Manager):
    """支持软删除的管理器"""

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, verbose_name="无序唯一标识")
    created_by = models.CharField(null=True, max_length=62, verbose_name="创建人")
    updated_by = models.CharField(null=True, max_length=62, verbose_name="更新人")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True
        verbose_name = '基础模型'
        verbose_name_plural = verbose_name
        ordering = ['-created_at']
