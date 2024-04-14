from django.db import models
from django.conf import settings

from common.base_model import BaseModel, SoftDeleteModel


class Role(BaseModel, SoftDeleteModel):
    identifier = models.CharField(verbose_name="角色唯一标识符", null=False, unique=True, db_index=True, max_length=32)
    name = models.CharField(verbose_name="角色名", null=True, max_length=32)
    description = models.TextField(null=True, blank=True, verbose_name="描述")
    is_active = models.BooleanField(verbose_name="启用/禁用", null=False, default=True, help_text="True 标识启用 False表示禁用")

    def __str__(self):
        return self.name

    class Meta:
        db_table = settings.TABLE_PREFIX + "role"
        verbose_name = "角色"
        verbose_name_plural = verbose_name


class RoleMenuPermission(models.Model):
    role = models.ForeignKey(
        to="Role",
        db_constraint=False,
        related_name="role_menu",
        on_delete=models.CASCADE,
        verbose_name="关联角色",
        help_text="关联角色",
    )
    menu = models.ForeignKey(
        to="permission.Menu",
        db_constraint=False,
        related_name="role_menu",
        on_delete=models.CASCADE,
        verbose_name="关联菜单",
        help_text="关联菜单",
    )

    class Meta:
        db_table = settings.TABLE_PREFIX + "role_menu"
        verbose_name = "角色菜单权限表"


class RoleMenuButtonPermission(models.Model):
    role = models.ForeignKey(
        to="Role",
        db_constraint=False,
        related_name="role_menu_button",
        on_delete=models.CASCADE,
        verbose_name="关联角色",
        help_text="关联角色",
    )
    menu_button = models.ForeignKey(
        to="permission.MenuButton",
        db_constraint=False,
        related_name="menu_button_permission",
        on_delete=models.CASCADE,
        verbose_name="关联菜单按钮",
        help_text="关联菜单按钮",
    )
    DATASCOPE_CHOICES = [
        (0, "仅本人数据权限"),
        (1, "本部门及以下数据权限"),
        (2, "本部门数据权限"),
        (3, "全部数据权限")
    ]
    data_range = models.IntegerField(default=0, choices=DATASCOPE_CHOICES, verbose_name="数据权限范围", help_text="数据权限范围")

    class Meta:
        db_table = settings.TABLE_PREFIX + "role_menuButton"
        verbose_name = "角色按钮权限表"
        verbose_name_plural = verbose_name
