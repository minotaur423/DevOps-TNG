def xyz(l):
    a=0
    for i in range(len(l)):
        a+=l[i]
        i+=1
    return a

listing = [ 1,2,3,4,5,6,7,8,9,10 ]
print(xyz(listing))
