# Implementation of bubble sort algorithm

# Time complexity O(n^2)
# Space complexity O(1)



def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    length = len(arr)
    
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    return arr


if __name__ == '__main__':
    arr = [9, 5, 1, 8, 4]
    print(f"Array is {arr}")
    bubble_sort(arr)
    print(f"Sorted array is {arr}")