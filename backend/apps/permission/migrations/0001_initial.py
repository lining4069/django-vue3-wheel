# Generated by Django 5.0.4 on 2024-04-15 08:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否被软删除', verbose_name='是否被软删除')),
                ('created_by', models.CharField(default='admin', max_length=64, null=True, verbose_name='创建人')),
                ('updated_by', models.CharField(default='admin', max_length=64, null=True, verbose_name='更新人')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('identifier', models.CharField(db_index=True, help_text='菜单唯一标识用于权限校验和授权', max_length=32, unique=True, verbose_name='标识')),
                ('name', models.CharField(help_text='菜单名称', max_length=64, null=True, verbose_name='菜单名称')),
                ('icon', models.CharField(help_text='菜单图标', max_length=64, null=True, verbose_name='菜单图标')),
                ('sort', models.IntegerField(default=1, help_text='显示排序', verbose_name='显示排序')),
                ('is_link', models.BooleanField(default=False, help_text='是否外链', verbose_name='是否外链')),
                ('link_url', models.CharField(help_text='链接地址', max_length=256, null=True, verbose_name='链接地址')),
                ('is_catalog', models.BooleanField(default=False, help_text='是否目录', verbose_name='是否目录')),
                ('web_path', models.CharField(help_text='路由地址', max_length=128, null=True, verbose_name='路由地址')),
                ('component', models.CharField(help_text='组件地址', max_length=128, null=True, verbose_name='组件地址')),
                ('component_name', models.CharField(help_text='组件名称', max_length=64, null=True, verbose_name='组件名称')),
                ('status', models.BooleanField(default=True, help_text='菜单状态', verbose_name='菜单状态')),
                ('cache', models.BooleanField(default=False, help_text='是否页面缓存', verbose_name='是否页面缓存')),
                ('visible', models.BooleanField(default=True, help_text='侧边栏中是否显示', verbose_name='侧边栏中是否显示')),
                ('is_iframe', models.BooleanField(default=False, help_text='框架外显示', verbose_name='框架外显示')),
                ('is_affix', models.BooleanField(default=False, help_text='是否固定', verbose_name='是否固定')),
                ('parent', models.ForeignKey(db_column='parent_id', db_constraint=False, help_text='上级菜单', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='permission.menu', verbose_name='上级菜单')),
            ],
            options={
                'verbose_name': '系统菜单表',
                'verbose_name_plural': '系统菜单表',
                'db_table': 'backend_system_menu',
            },
        ),
        migrations.CreateModel(
            name='MenuButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否被软删除', verbose_name='是否被软删除')),
                ('created_by', models.CharField(default='admin', max_length=64, null=True, verbose_name='创建人')),
                ('updated_by', models.CharField(default='admin', max_length=64, null=True, verbose_name='更新人')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('identifier', models.CharField(db_index=True, help_text='接口唯一标识用于权限校验和授权', max_length=32, unique=True, verbose_name='权限值')),
                ('name', models.CharField(help_text='名称', max_length=64, verbose_name='按钮名称')),
                ('api', models.CharField(help_text='按钮绑定的接口地址', max_length=512, verbose_name='接口地址')),
                ('method', models.IntegerField(choices=[(0, 'GET'), (1, 'POST'), (2, 'PUT'), (3, 'DELETE')], default=0, help_text='接口请求方法', null=True, verbose_name='接口请求方法')),
                ('menu', models.ForeignKey(db_column='menu_id', db_constraint=False, help_text='关联菜单', on_delete=django.db.models.deletion.CASCADE, related_name='menuPermission', to='permission.menu', verbose_name='关联菜单')),
            ],
            options={
                'verbose_name': '系统接口表',
                'verbose_name_plural': '系统接口表',
                'db_table': 'backend_system_menuButton',
            },
        ),
    ]
