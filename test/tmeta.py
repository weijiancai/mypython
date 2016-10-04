import mu.core.meta as meta
import mu.core.dict as ddict

meta.define('DataSource', '数据源', [
    meta.MetaField('ID', 'ID'),
    meta.MetaField('name', '名称'),
    meta.MetaField('displayName', '显示名'),
    meta.MetaField('desc', '描述'),
    meta.MetaField('type', '类型', dict_id=ddict.get('DataSourceType').uid),
    meta.MetaField('url', 'URL'),
    meta.MetaField('host', '主机'),
    meta.MetaField('port', '端口'),
    meta.MetaField('userName', '用户名'),
    meta.MetaField('pwd', '密码'),
    meta.MetaField('isValid', '是否有效'),
    meta.MetaField('sortNum', '排序号'),
    meta.MetaField('inputDate', '录入时间')
])


for meta in meta.metaList:
    print(meta)