import pdb

def bubble_sort(array):
    length = len(array)
    for pass_number in range(length):
        for current_index in range(0, length - pass_number - 1):  # Last `pass_number` elements are already sorted
            if array[current_index] > array[current_index + 1]:
                array[current_index], array[current_index + 1] = array[current_index + 1], array[current_index]  # Swap
                print(f"Swapped {array[current_index]} and {array[current_index + 1]}: {array}")
    return array

# Test
test_array = [12, 5, 2, 9, 1, 10, 3]
#print("Bubble Sort - Initial Array:", test_array)
#print("Bubble Sort - Sorted Array:", bubble_sort(test_array))
def selection_sort(array):
    length = len(array)
    for start_index in range(length):
        min_index = start_index
        for current_index in range(start_index + 1, length):
            if array[current_index] < array[min_index]:
                min_index = current_index  # Find the minimum element
        array[start_index], array[min_index] = array[min_index], array[start_index]  # Swap
        print(f"Placed {array[start_index]} at position {start_index}: {array}")
    return array

# Test
test_array = [64, 34, 25, 12, 22, 11, 90]
#print("Selection Sort - Initial Array:", test_array)
#print("Selection Sort - Sorted Array:", selection_sort(test_array))

def insertion_sort(array):
    for index in range(1, len(array)):
        #pdb.set_trace()
        key_value = array[index]
        position = index - 1
        while position >= 0 and key_value < array[position]:
            array[position + 1] = array[position]
            position -= 1
            print(f"Moved {array[position + 1]} to position {position + 2}: {array}")
        array[position + 1] = key_value
        print(f"Inserted {key_value} at position {position + 1}: {array}")
    return array

# Test
test_array = [7, 5,2, 0, 8, -10]
#print("Insertion Sort - Initial Array:", test_array)
#print("Insertion Sort - Sorted Array:", insertion_sort(test_array))
#pdb.set_trace()

def merge_sort(array):
    print(f"vinod0 first array {array}")
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        print(f"vinod1 left array {left_half}")
        right_half = array[mid:]
        print(f"vinod2 right array {right_half}")

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        print(f"vinod3 first while {i < len(left_half) and j < len(right_half)} i: {i} {left_half} j: {j} {right_half}")
        while i < len(left_half) and j < len(right_half):
            print(f"vinod4 first if {left_half[i] < right_half[j]} {left_half[i]} {right_half[j]}")
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        print(f"vinod5 second while loop {i < len(left_half)} i: {i} k: {k} left array {left_half}")
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        print(f"vinod6 third while loop {j < len(right_half)} j: {j} k: {k} right array {right_half}")
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
        print(f"Merged {left_half} and {right_half} into {array}")
    return array

# Test
#test_array = [2,0,1,6,-10]
#test_array = [20,15,11,16,12,14,18,17,19,13,10,1,5,2,3,9,4,8,7,6,5]
test_array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#print("Merge Sort - Initial Array:", test_array)
#print("Merge Sort - Sorted Array:", merge_sort(test_array))

def recursion_example(array, name):
    #print(f"vinod0 first array {array}")
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        print(f"vinod1 left array {left_half}")
        recursion_example(left_half, "left")
        print(f"vinod2 left array {left_half}")
        print(f"vinod3 right array {right_half}")
        recursion_example(right_half, "right")
        print(f"vinod4 right array {right_half}")
    else:
        print(f"recursion is completed {name}")

#recursion_example(test_array, "main")


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left_part = [x for x in array if x < pivot]
    middle_part = [x for x in array if x == pivot]
    right_part = [x for x in array if x > pivot]
    print(f"Pivot: {pivot}, Left: {left_part}, Middle: {middle_part}, Right: {right_part}")
    return quick_sort(left_part) + middle_part + quick_sort(right_part)

# Test
#test_array = [10, 7, 8, 9, 1, 5]
print("Quick Sort - Initial Array:", test_array)
print("Quick Sort - Sorted Array:", quick_sort(test_array))
