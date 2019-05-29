

array = [1, 10, 5, 4, 9, 20, 12, 3, 7, 11]

# 寻找N个元素中的前K个最大者
# 例子: 前3个


def quick_sort(array, left, right, k):
    if left >= right:
        return
    i, j, pivot = left, right, array[left]

    while i < j:
        while i < j and array[j] >= pivot:
            j -= 1
        while i < j and array[i] <= pivot:
            i += 1
        array[i], array[j] = array[j], array[i]
    array[left], array[i] = array[i], array[left]

    if right - (i + 1) + 1 + 1 < k:
        quick_sort(array, left, i - 1, k)
    quick_sort(array, i + 1, right, k)


quick_sort(array, 0, len(array) - 1, 3)
print(array)
print(array[-3:])
print(array[:-4:-1])
