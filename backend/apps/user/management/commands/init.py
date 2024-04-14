# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 6:26 PM
# @Author : lining
# @Remark : 系统初始化数据 fe： 默认用户、默认组、默认角色
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from apps.user.models import User
from apps.group.models import Group
from apps.role.models import Role


class Command(BaseCommand):
    help = '初始化数据库中...'

    def handle(self, *args, **options):
        # 建立默认角色
        default_role_obj = Role.objects.create(
            id=1,
            identifier="default_role",
            name="默认角色",
            description="系统自动生成默认角色",
            is_active=True,
        )
        default_role_obj.save()

        # 赋予默认橘色应当具备的菜单和api权限。

        # 建立默认组
        default_group_obj = Group.objects.create(
            id=1,
            parent_id=None,
            identifier="default_group",
            name="默认组",
            description="系统自动生成默认组",
            leader=None,
            is_active=True
        )

        # 将默认组绑定上默认角色
        default_group_obj.roles.set([default_role_obj])

        # 创建系统初始普通用户
        init_user = User.objects.create(
            username="init_sample_user",
            display_name="初始化普通用户",
            password=make_password("Aa123456"),
            gender=0,
            source=0,
            email="xxxxxx@xx.com",
            is_active=True
        )
        init_user.groups.set([default_group_obj])
        init_user.roles.set([default_role_obj])
        init_user.save()

        # role中建立name为默认角色
        self.stdout.write(self.style.SUCCESS('成功完成系统初始化'))
