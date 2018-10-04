def xyz():
    l = []
    i = 10
    count = 0
    while i >= 0:
        l.insert(count,i)
        i-=1
        count+=1
    return l

print(xyz())
