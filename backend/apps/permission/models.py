from django.db import models
from django.conf import settings

from common.base_model import BaseModel, SoftDeleteModel


class Menu(BaseModel, SoftDeleteModel):
    """菜单"""
    parent = models.ForeignKey(
        null=True,
        to="Menu",
        on_delete=models.DO_NOTHING,  # 处理逻辑同用户组
        related_name="children",
        db_column="parent_id",
        db_constraint=False,
        verbose_name="上级菜单",
        help_text="上级菜单",
    )
    identifier = models.CharField(verbose_name="标识", unique=True, db_index=True, max_length=32, help_text="菜单唯一标识用于权限校验和授权")
    name = models.CharField(verbose_name="菜单名称", null=True, max_length=64, help_text="菜单名称")
    icon = models.CharField(verbose_name="菜单图标", null=True, max_length=64, help_text="菜单图标")
    sort = models.IntegerField(verbose_name="显示排序", default=1, help_text="显示排序")
    is_link = models.BooleanField(verbose_name="是否外链", default=False, help_text="是否外链")
    link_url = models.CharField(verbose_name="链接地址", null=True, max_length=256, help_text="链接地址")
    is_catalog = models.BooleanField(verbose_name="是否目录", default=False, help_text="是否目录")
    web_path = models.CharField(verbose_name="路由地址", null=True, max_length=128, help_text="路由地址")
    component = models.CharField(verbose_name="组件地址", null=True, max_length=128, help_text="组件地址")
    component_name = models.CharField(verbose_name="组件名称", null=True, max_length=64, help_text="组件名称")
    status = models.BooleanField(verbose_name="菜单状态", default=True, help_text="菜单状态")
    cache = models.BooleanField(verbose_name="是否页面缓存", default=False, help_text="是否页面缓存")
    visible = models.BooleanField(verbose_name="侧边栏中是否显示", default=True, help_text="侧边栏中是否显示")
    is_iframe = models.BooleanField(verbose_name="框架外显示", default=False, help_text="框架外显示")
    is_affix = models.BooleanField(verbose_name="是否固定", default=False, help_text="是否固定")

    class Meta:
        db_table = settings.TABLE_PREFIX + "system_menu"


class MenuButton(BaseModel, SoftDeleteModel):
    """菜单按钮"""
    menu = models.ForeignKey(
        to="Menu",
        on_delete=models.CASCADE,
        related_name="menuPermission",
        db_column="menu_id",
        db_constraint=False,
        verbose_name="关联菜单",
        help_text="关联菜单",
    )
    identifier = models.CharField(verbose_name="权限值", unique=True, db_index=True, max_length=32, help_text="接口唯一标识用于权限校验和授权")
    name = models.CharField(verbose_name="按钮名称", max_length=64, help_text="名称")
    api = models.CharField(verbose_name="接口地址", max_length=512, help_text="按钮绑定的接口地址")
    METHOD_CHOICES = [
        (0, "GET"),
        (1, "POST"),
        (2, "PUT"),
        (3, "DELETE"),
    ]
    method = models.IntegerField(verbose_name="接口请求方法", default=0, choices=METHOD_CHOICES, null=True, help_text="接口请求方法")

    class Meta:
        db_table = settings.TABLE_PREFIX + "system_menuButton"
        ordering = ("-name",)
