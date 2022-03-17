def recursearch(L,k,begin,end):
    '''This will recursively compute binary search'''
    if begin==end:
        if L[begin]==k:
            return 1
        else:
            return 0
    if end-begin==1:
        if L[begin]==k or L[end]==k:
            return 1
        else:
            return 0
    if end-begin>1:
        mid=(begin+end)//2
        if L[mid]>k:
            end=mid-1
        elif L[mid]<k:
            begin=mid+1
        elif L[mid]==k:
            return 1
    if end-begin<0:
        return 0
    return recursearch(L,k,begin,end)

L=list(range(100000))
print(recursearch(L,-1234,0,len(L)-1))
