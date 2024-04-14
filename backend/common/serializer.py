# -*- coding: utf-8 -*-
# @Project : django-vue3-wheel
# @Env : PyCharm
# @Create At : 2024/4/14 1:05 PM
# @Author : lining
# @Remark : 基础序列化类
from rest_framework import serializers
from common.base_model import BaseModel


class OpsBaseModelSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_by = serializers.CharField(read_only=True)
    updated_by = serializers.CharField(read_only=True)

    def create(self, validated_data):
        # 处理创建人和更新人
        validated_data['founder'] = self.context.get('request').user.username
        validated_data['updater'] = self.context.get('request').user.username
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # 处理组更新人
        validated_data['updater'] = self.context.get('request').user.username
        return super().update(instance, validated_data)

    class Meta:
        model = BaseModel
        fields = '__all__'
