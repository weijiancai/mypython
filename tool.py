def findStr(fileName, str):
    f = open(fileName, 'r')
    i = 0
    for line in f:
        i += 1
        if(line.find(str) >= 0):
            print('%i     %s' % (i, line))