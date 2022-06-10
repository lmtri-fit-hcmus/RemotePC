def Help():
    f = open('Help.txt', 'r')
    lines = f.readlines()
    result = ""
    for l in lines:
        result = result + l
    f.close()
    return result
