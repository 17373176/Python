# merge sort
# 归并排序

def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = int(len(list)/2)
    left = merge_sort(list[:middle])
    right = merge_sort(list[middle:])
    merged = []    # 定义一个空列表
    while left and right: #如果左右两个列表都不空的时候
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0)) #左列表元素比右列表元素小的加入到merged列表中
    merged.extend(right if right else left) #将剩余列表元素添加至merged中
    return  merged

# main function
list = [6, 202, 100, 301, 38, 8, 1]
print(merge_sort(list))