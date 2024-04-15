# Generated by Django 5.0.4 on 2024-04-15 04:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('role', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False, help_text='是否被软删除', verbose_name='是否被软删除')),
                ('created_by', models.CharField(default='admin', max_length=64, null=True, verbose_name='创建人')),
                ('updated_by', models.CharField(default='admin', max_length=64, null=True, verbose_name='更新人')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('identifier', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='组唯一标识符')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='组名')),
                ('description', models.TextField(default=None, null=True, verbose_name='备注')),
                ('leader', models.IntegerField(help_text='部门领导用户id,标识作用非关联关系作用,不使用外键', null=True, verbose_name='部门leader')),
                ('is_active', models.BooleanField(default=True, help_text='True 标识启用 False表示禁用', verbose_name='启用/禁用')),
                ('parent', models.ForeignKey(db_column='parent_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children', to='group.group', verbose_name='上级部门/用户组')),
                ('roles', models.ManyToManyField(blank=True, db_constraint=False, related_name='role_groups', to='role.role', verbose_name='角色')),
            ],
            options={
                'verbose_name': '组',
                'verbose_name_plural': '组',
                'db_table': 'backend_group',
            },
        ),
    ]
