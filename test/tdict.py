import mu.core.dict as ddict

ddict.define('MetaDataType', '数据类型', [
    {"name": "STRING", "displayName": "字符串"},
])

ddict.define('DisplayStyle', '显示样式', [
    ddict.code('TEXT_FIELD', '文本框'),
    ddict.code('TEXT_AREA', '文本域'),
])

ddict.define('DataSourceType', '数据源类型', [
    ddict.code('DATABASE', '数据库'),
    ddict.code('FILE_SYSTEM', '文件系统'),
    ddict.code('UNKNOWN', '未知')
])

for aDict in ddict.dictMap:
    print(aDict)