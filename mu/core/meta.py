class MetaItem:
    id = 0
    name = ''
    displayName = ''
    dataType = ''
    category = ''
    maxLength = 0
    desc = ""
    isValid = True
    sortNum = 0
    inputDate = None

    def __init__(self, id, name):
        self.id = id
        self.name = name
