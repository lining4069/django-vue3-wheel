from django.db import models
from django.conf import settings

from common.model import BaseModel, SoftDeleteModel


class Group(BaseModel, SoftDeleteModel):
    """
    用户组模型
    """
    parent = models.ForeignKey(
        to="self",
        on_delete=models.DO_NOTHING,  # 当上级用户组/部门被删除时其下级用户组自动上移层次结构
        null=True,
        db_constraint=False,
        db_column="parent_id",
        related_name="children",
        verbose_name="上级部门/用户组",
    )
    name = models.CharField(verbose_name="组名", null=True, max_length=62)
    description = models.TextField(default=None, null=True, verbose_name="备注")
    leader = models.CharField(verbose_name="部门leader", null=True, max_length=32, help_text="部门领导用户id,标识作用非关联关系作用,不使用外键")
    is_active = models.BooleanField(verbose_name="启用/禁用", null=False, default=True, help_text="True 标识启用 False表示禁用")

    roles = models.ManyToManyField(
        to="role.Role",
        related_name="role_groups",
        db_constraint=False,
        blank=True,
        verbose_name="角色",
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = settings.TABLE_PREFIX + "group"
        verbose_name = "组"
        verbose_name_plural = verbose_name
