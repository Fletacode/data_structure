

def findMax(li):

    st = 0
    end = len(li)

    while st <= end:
        mid = (st+end) // 2
        

        if mid > 0 and mid < len(li) - 1:
            if li[mid] > li[mid-1] and li[mid] > li[mid+1]:
                return li[mid]
            elif li[mid] < li[mid+1]:
                st = mid + 1
            else:
                end = mid - 1

        elif mid == len(li) - 1:
            if li[mid] > li[mid-1]:
                return li[mid]
            else:
                return li[mid-1]
        elif mid == 0:
            if li[mid] > li[mid+1]:
                return li[mid]
            else:
                return li[mid+1]
            




if __name__ == "__main__":
    li = [2,4,8,10,7,5,3]

    print(findMax(li))
    print(findMax([1,2]))
    print(findMax([2,1]))