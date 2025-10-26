import time
import random
import logging
import matplotlib.pyplot as plt
import matplotlib.animation as animation


logging.basicConfig(level=logging.INFO, filename="LR_3_log.log", filemode="w", format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')

def bubble_sort(nums):
    start_time = time.time()
    frames = []
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                frames.append(nums.copy())
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения: {execution_time:.6f} секунд")
    visualize_sort(frames)


def selection_sort(nums):
    start_time = time.time()
    frames = []
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        frames.append(nums.copy())
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения: {execution_time:.6f} секунд")
    visualize_sort(frames)


def insertion_sort(nums):
    start_time = time.time()
    frames = []
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
        frames.append(nums.copy())
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения: {execution_time:.6f} секунд")
    visualize_sort(frames)


def heapify(nums, heap_size, root_index, frames=None):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        if frames is not None:
            frames.append(nums.copy())
        heapify(nums, heap_size, largest, frames)

def heap_sort(nums):
    start_time = time.time()
    frames = []
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i, frames)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0, frames)
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения: {execution_time:.6f} секунд")
    visualize_sort(frames)


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):
    frames = []
    temp = nums.copy()  

    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right, temp)
            frames.append(arr.copy())

    merge_sort_helper(nums, 0, len(nums) - 1)
    visualize_sort(frames)
    return nums

def merge(arr, left, mid, right, temp):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    start_time = time.time()
    frames = []
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            frames.append(items.copy())
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)
    _quick_sort(nums, 0, len(nums) - 1)
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"Время выполнения: {execution_time:.6f} секунд")
    visualize_sort(frames)


def visualize_sort(frames):
    plt.ion()  
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(frames[0])), frames[0], color='skyblue')
    ax.set_title("Визуализация сортировки")
    ax.set_xlabel("Индекс")
    ax.set_ylabel("Значение")

    for frame in frames:
        for bar, height in zip(bars, frame):
            bar.set_height(height)
        plt.pause(0.3) 

    plt.ioff()
    plt.show()


n = int(input('Введи количество элементов в списке: '))
list = []
for i in range (n):
    a = random.randint(1, 100)
    list += [a]
s = 100
print ('Вариант сортировки: 1 - пузырьком, 2 - выборкой, 3 - вставками, 4 - пирамидой, 5 - слиянием, 6 - быстрой сортировкой')
s = int(input())
if s == 1:
    bubble_sort(list)
elif s == 2:
    selection_sort(list)
elif s ==3:
    insertion_sort(list)
elif s == 4:
    heap_sort(list)
elif s == 5:
    merge_sort(list)
elif s == 6:
    quick_sort(list)
