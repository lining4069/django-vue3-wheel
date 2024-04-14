from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings

from common.base_model import BaseModel, SoftDeleteModel


# 用户表


class User(AbstractBaseUser, BaseModel, SoftDeleteModel):
    username_validator = UnicodeUsernameValidator()
    SOURCE_TYPE_CHOICES = [(0, "本地用户"), (1, "AD域账号")]
    GENDER_CHOICES = [(0, "未知"), (1, "男"), (2, "女")]

    username = models.CharField(verbose_name="用户名", max_length=150, unique=True, db_index=True, validators=[username_validator],
                                error_messages={"unique": "该用户已存在"})
    display_name = models.CharField(verbose_name="显示名", max_length=150, null=True)
    password = models.CharField(verbose_name="密码", max_length=16, null=True)  # 至少八位
    gender = models.IntegerField(verbose_name="性别", choices=GENDER_CHOICES, default=0, null=True, blank=True, help_text="性别")
    source = models.IntegerField(verbose_name="用户来源", choices=SOURCE_TYPE_CHOICES, default=0, null=False)
    last_deactivate = models.DateTimeField(verbose_name="最近用户被禁用时间", null=True)
    last_login = models.DateTimeField(verbose_name="最后登录时间", null=True)
    last_change_password = models.DateTimeField(verbose_name="最后修改密码时间", null=True)

    groups = models.ManyToManyField(
        to="group.Group",
        related_name="group_users",
        blank=True,
        db_constraint=False,
        verbose_name="用户组"
    )
    roles = models.ManyToManyField(
        to="role.Role",
        related_name="role_users",
        blank=True,
        db_constraint=False,
        verbose_name="角色"
    )

    def __str__(self):
        return self.username

    USERNAME_FIELD = "username"

    class Meta:
        db_table = settings.TABLE_PREFIX + "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        unique_together = ("username",)
