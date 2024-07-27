# Implementation of bubble sort algorithm

# Time complexity O(n^2)
# Space complexity O(1)



def Inseration_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    length = len(arr)

    # example
    # i = 4
    # 1, 2, 4, (5, 3)
    # 1, 2, (4, 3), 5   
    # 1, (2, 3), 4, 5
    
    for i in range(length):
        if i != 0:   #assume first element is in the "sorted list"
            for j in range(i):
                if arr[i - j] < arr[i - j - 1]:
                    temp = arr[i - j]
                    arr[i - j] = arr[i - j - 1]
                    arr[i - j - 1] = temp
    
    return arr


if __name__ == '__main__':
    arr = [9, 5, 1, 8, 4]
    print(f"Array is {arr}")
    Inseration_sort(arr)
    print(f"Sorted array is {arr}")