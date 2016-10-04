# encoding: utf-8
# module meta

import datetime
import uuid
from enum import Enum

__all__ = ['Meta']

# enums


class MetaDataType(Enum):
    STRING = 0  # 字符串
    INTEGER = 1  # 

# classes


class MetaItem:
    """ 元数据项 """

    def __init__(self, _id=0, name='', display_name='', desc='', category='', is_valid=True, sort_num=0,
                 input_date=datetime.datetime.now()):
        self.id = _id  # ID
        self.name = name  # 名称
        self.displayName = display_name  # 显示名
        self.desc = desc  # 描述
        self.category = category  # 分类
        self.isValid = is_valid  # 是否有效
        self.sortNum = sort_num  # 排序号
        self.inputDate = input_date  # 录入时间


class Meta:
    """ 元数据 """

    def __init__(self, name, display_name, fields, desc='', is_valid=True, sort_num=0,
                 input_date=datetime.datetime.now()):
        self.id = uuid.uuid1()  # ID
        self.name = name  # 名称
        self.displayName = display_name  # 显示名
        self.desc = desc  # 描述
        self.isValid = is_valid  # 是否有效
        self.sortNum = sort_num  # 排序号
        self.inputDate = input_date  # 录入时间
        self.fields = fields  # 元数据字段

    def __str__(self):
        return "Meta{id: %s, name: %s, displayName: %s, fields: [\n%s\n]}" \
               % (self.id, self.name, self.displayName, '\n'.join(str(field) for field in self.fields))


class MetaField(object):
    """ 元数据字段 """

    def __init__(self, name, display_name, desc='', data_type=MetaDataType.STRING, default_value='',
                 dict_id='', max_length=0, is_pk=False, is_fk=False, is_require=False,
                 is_valid=True, sort_num=0, input_date=datetime.datetime.now()):
        self.id = uuid.uuid1()  # ID
        self.name = name  # 名称
        self.displayName = display_name  # 显示名
        self.desc = desc  # 描述
        self.dataType = data_type  # 数据类型
        self.defaultValue = default_value  # 默认值
        self.dictId = dict_id  # 数据字典
        self.maxLength = max_length  # 最大长度
        self.isPk = is_pk  # 是否主键
        self.isFk = is_fk  # 是否外键
        self.isRequire = is_require  # 是否必须
        self.isValid = is_valid  # 是否有效
        self.sortNum = sort_num  # 排序号
        self.inputDate = input_date  # 录入时间

    def __str__(self):
        return "MetaField{id: %s, name: %s, displayName: %s, dict_id: %s}" \
               % (self.id, self.name, self.displayName, self.dictId)


# variables

metaList = []


def define(name, display_name, fields):
    metaList.append(Meta(name, display_name, fields))


define('Meta', '元数据', [
    {"id": 1, "name": 'ID', "displayName": "ID", "isPk": True},
    {"id": 2, "name": 'name', "displayName": "名称"},
    {"id": 3, "name": 'displayName', "displayName": "显示名"}
])


define('People', 'People', [
    MetaField('ID', 'ID')
])


print(metaList)

