def quick_sort(alist, first, last):         #原地排序
    if first >= last:   #当只有一个数的时候不用排序
        return
    mid = alist[first]  #最左边的数设为分界点
    low = first
    high = last     #两个移动的指针
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] = alist[high]        #先右边再左边，而且由于alist[low]已经存起来了所以不用担心覆盖掉
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid        #当low==high后, 记得将分界点 也就是第一个数 移动到中间来
    quick_sort(alist, first, low-1)     #mid位置已经确定了，只需要管两边
    quick_sort(alist, low+1, last)

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
quick_sort(numbers,0,len(numbers)-1)
assert numbers == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]