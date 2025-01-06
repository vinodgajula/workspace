import pdb
array_sample = [1,2,3,4,5,3,33,333]

def array_traversal(arr):
    for element in arr:
        print(f"traversal of array: {element}")

def reverse_array(array):
    for number in range(1, len(array)+1):
        print(f"reverse array elements: {array[-number]}")

def count_array_element(element, array):
    count = 0
    for element_value in array:
        if element == element_value:
            #pdb.set_trace()
            count = count+1
    print(f"count of element {element} is {count}")


def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index of the target
    return -1  # Element not found

# Test Cases
array = [3, 1, 4, 1, 5, 9, 2, 6]
target = 5

result = linear_search(array, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

def binary_search(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1  
        elif mid_number > query:
            lo = mid + 1
    
    return -1

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):  # Last i elements are already sorted
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
    return arr

# Test
array = [5, 2, 9, 1, 5, 6]
#print("Sorted Array:", bubble_sort(array))

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # Find the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
    return arr

# Test
array = [64, 34, 25, 12, 22, 11, 90]
print("Sorted Array:", selection_sort(array))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test
array = [12, 11, 13, 5, 6]
print("Sorted Array:", insertion_sort(array))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Test
array = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(array))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test
array = [10, 7, 8, 9, 1, 5]
print("Sorted Array:", quick_sort(array))


#count_array_element(3, array_sample)
#reverse_array(array_sample)