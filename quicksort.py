def partition(arr,p,q):
    #lo、hi分别表示指向首个元素和倒数第 2 个元素的索引
    lo = p
    hi = q
    #pivot 表示选中的中间值
    pivot = arr[q]
    while lo < hi:
        #lo从左往右遍历，直至找到一个不小于 pivot 的元素
        while lo < hi and arr[lo] <= pivot:
            lo = lo + 1
        #hi从右往左遍历，直至找到一个不大于 pivot 的元素
        while lo < hi and arr[hi] >= pivot:
            hi = hi - 1
            #交换 arr[lo] 和 arr[hi] 的值
        arr[lo],arr[hi] = arr[hi],arr[lo]
    #交换 arr[lo] 和 arr[q] 的值
    arr[lo],arr[q] = arr[q],arr[lo]
    # print(arr)
    #返回中间值所在序列中的位置
    return lo

def quick_sort(arr,p,q):
    #如果待排序序列不存在，或者仅包含 1 个元素，则不再进行分割
    if p >= q:
        return
    #调用 partition() 函数，分割 [p,q] 区域
    par = partition(arr,p,q)
    #以 [p,par-1]作为新的待排序序列，继续分割
    quick_sort(arr,p,par-1)
    #以[par+1,q]作为新的待排序序列，继续分割
    quick_sort(arr,par+1,q)
  
arr=[35,33,42,10,14,19,27,44,26,31]
#对于 arr 列表中所有元素进行快速排序
quick_sort(arr,0,len(arr)-1)
print(arr)