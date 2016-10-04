import uuid

# classes


class DataDict(object):
    """ import ddict
        define('MetaDataType', 'MetaDataType', [{name:'STRING', displayName:'字符串'},
        {name:'INTEGER', displayName:'整数'}])
    """
    def __init__(self, name, display_name, _codes, category='', pid=None):
        self.uid = uuid.uuid1()  # UUID
        self.name = name
        self.displayName = display_name
        self.category = category
        self.pid = pid
        self.codes = []

        sort_num = 0
        for code in _codes:
            sort_num += 1
            if isinstance(code, dict):
                print('code is dict')
                self.codes.append(DictCode(code['name'], code['displayName'], self.uid, sort_num))
            elif isinstance(code, DictCode):
                print('code is DictCode')
                self.codes.append(code)

    def __str__(self):
        return "DataDict{id: %s, name: %s, displayName: %s, codes: [\n%s\n]}" \
               % (self.uid, self.name, self.displayName, '\n'.join(str(code) for code in self.codes))


class DictCode(object):
    def __init__(self, name, display_name, dict_id='', sort_num=0):
        self.uid = uuid.uuid1()  # UUID
        self.name = name
        self.displayName = display_name
        self.sortNum = sort_num
        self.dictId = dict_id

    def __str__(self):
        return "DictCode{id: %s, name: %s, displayName: %s}" \
               % (self.uid, self.name, self.displayName)

# variables

dictMap = dict()


def define(name, display_name, codes):
    dictMap[name] = DataDict(name, display_name, codes)


def code(name, display_name):
    return DictCode(name, display_name)


def get(name):
    return dictMap.get(name)


define('DataSourceType', '数据源类型', [
    DictCode('DATABASE', '数据库'),
    DictCode('FILE_SYSTEM', '文件系统'),
    DictCode('UNKNOWN', '未知')
])