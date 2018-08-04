def bsearch(list,val):
    list_size = len(list) - 1
    index0 = 0
    indexn = list_size

    while index0 <= indexn:
        midval = (index0+indexn)//2

        if list[midval] == val:
            return(midval)

        if val > list[midval]:
            index0 = midval + 1
        else:
            indexn = midval - 1

    if index0 > indexn:
        return None

list = sorted([1,54,6,79,234,5,990,12,34,3,7,66,24])


print(bsearch(list,54))








