# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 6:26 PM
# @Author : lining
# @Remark : 系统初始化数据 fe： 默认用户、默认组、默认角色
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from apps.role.models import Role
from apps.group.models import Group
from apps.user.models import User


class Command(BaseCommand):
    help = '初始化数据库'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('开始进行数据库初始化...'))
        self.stdout.write(self.style.SUCCESS('建立默认角色、组和普通用户(绑定默认组和默认角色)...'))
        # 建立默认角色
        default_role_ins = Role.objects.filter(identifier__exact="default_role").first()
        if default_role_ins is None:
            default_role_ins = Role.objects.create(
                id=1,
                identifier="default_role",
                name="默认角色",
                description="系统自动生成默认角色",
                is_active=True,
            )
            default_role_ins.save()

        # 建立默认组
        default_group_ins = Group.objects.filter(identifier__exact="default_group").first()
        if default_group_ins is None:
            default_group_ins = Group.objects.create(
                id=1,
                parent_id=None,
                identifier="default_group",
                name="默认组",
                description="系统自动生成默认组",
                leader=None,
                is_active=True
            )
            # 将默认组绑定上默认角色
            default_group_ins.roles.set([default_role_ins])
            default_group_ins.save()

        # 创建系统初始普通用户
        sys_super_user = User.objects.filter(is_superuser=True).first()
        if sys_super_user is None:
            sys_super_user = User.objects.create(
                username="superadmin",
                display_name="超级管理员",
                password=make_password("Admin123456"),
                email="admin@localhost"
            )
            sys_super_user.save()
        init_user_ins = User.objects.filter(username__exact="init_sample_user").first()
        if init_user_ins is None:
            init_user_ins = User.objects.create(
                username="init_sample_user",
                display_name="初始化普通用户",
                password=make_password("Aa123456"),
                email="xxxxxx@xx.com",
                is_active=True
            )
            init_user_ins.groups.set([default_group_ins])
            init_user_ins.roles.set([default_role_ins])
            init_user_ins.save()

        self.stdout.write(self.style.SUCCESS("建立默认角色、默认组和普通用户正常"))
        # role中建立name为默认角色
        self.stdout.write(self.style.SUCCESS('系统初始化正常完成'))
