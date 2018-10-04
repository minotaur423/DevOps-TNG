def xyz(l):
    a = 7
    retcode = "no"
    for i in range(len(l)):
        if l[i] == a:
            retcode = "Bingo"
    return retcode

listing = [ 1,2,3,4,5,6,8 ]
print(xyz(listing))
