list_1 = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
# Search using linear search for 9 in list_1 and print the index of the element if found, otherwise print that it is not found.
def linear_search(lst, target):
    for index in range(len(lst)):
        if lst[index] == target:
            return index
    return None
# Search for the number 9 in list_1 and print the result.
search_number = 9
result = linear_search(list_1, search_number)
if result is not None:
    print(f"{search_number} is found at index {result}.")
else:
    print(f"{search_number} is not found in the list.")
    # Reason for choosing linear seach algorithm: 
    # Linear search is a simple algorithm that checks each element in the list sequentially until it finds the target or reaches the end of the list. 
    # It is suitable for small lists or when the list is unsorted, as it does not require any preprocessing. 
    # In this case, since list_1 is unsorted and contains only 14 elements, linear search is an efficient choice for finding the number 9.

# Implement the Insertion sort on this list.

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst
# Sort list_1 using insertion sort and print the sorted list.
sorted_list = insertion_sort(list_1)
print("Sorted list:", sorted_list)  

# Implement a binary search algorithm to search for the number 9 in the sorted list and print the index of the element if found, otherwise print that it is not found.
def binary_search(lst, target):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

search_number = 9
result = binary_search(sorted_list, search_number)
if result is not None:
    print(f"{search_number} is found at index {result}.")
else:
    print(f"{search_number} is not found in the sorted list.")
    # Reason for choosing binary search algorithm:
    # Binary search is an efficient algorithm for finding an element in a sorted list. It works by repeatedly dividing the search interval in half, which allows it to quickly narrow down the possible locations of the target element. 
    # In this case, since the list is sorted using insertion sort, binary search is an appropriate choice for finding the number 9, as it will significantly reduce the number of comparisons needed compared to linear search, especially as the size of the list increases.
    # Real-world use: Sorting large datasets by length is common in applications like text processing, where you might want to prioritize longer strings for display or analysis. For example, in a search engine, you might want to sort search results by the length of the content to provide more comprehensive results at the top. In such cases, using an efficient sorting algorithm like merge sort can help manage large datasets effectively.