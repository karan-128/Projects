def binary_search(L,k):
    #Pre-requisite: List L must be sorted
    #check middle element and find if 'k' is on the left or right of the middle element
    #to get middle element, take (first + last element)/2
    begin=0      #Position of first element of L
    end=len(L)-1 #Position of last element of L
    while(end-begin>1): #while end-begin has at least 2 elements
        mid=(begin+end)//2
        #if middle element is equal to k
        if L[mid]==k:
            return 1
        #if middle element is greater than k, then remove the right part from the list
        if L[mid]>k:
            end=mid-1 #mid element becomes the endpoint for new list
        else:
            begin=mid+1
    if L[begin]==k or L[end]==k:
        return 1
    else:
        return 0



