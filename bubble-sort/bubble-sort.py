# Implementation of bubble sort algorithm





def bubble_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    return 0


if __name__ == '__main__':
    arr = [3, 5, 1, 8, 3]
    bubble_sort(arr)
    print(f"Sorted array is {arr}")