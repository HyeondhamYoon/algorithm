# 힙 성질을 만족하는지 확인
def heapify(unsorted, index, heap_size):
    largest = index

    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index

    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)


def heap_sort(unsorted):
    n = len(unsorted)
    print("Before Max Heap : ", unsorted)

    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    print("After Max Heap : ", unsorted, "\n")

    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
        print("DownHeap", n-i, " : ", unsorted)
    return unsorted


data = [40, 10, 50, 90, 20, 80, 30, 60]
heap_sort(data)
print("\nResult : ", data)