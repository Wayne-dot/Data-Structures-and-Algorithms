from insertion_sort import Inseration_sort

# Test cases
def test_binseration_sort():
    # Test case 1: Regular unsorted list
    arr = [9, 5, 1, 8, 4]
    assert Inseration_sort(arr.copy()) == [1, 4, 5, 8, 9], "Test case 1 failed"
    
    # Test case 2: Already sorted list
    arr = [1, 2, 3, 4, 5]
    assert Inseration_sort(arr.copy()) == [1, 2, 3, 4, 5], "Test case 2 failed"
    
    # Test case 3: Reverse sorted list
    arr = [5, 4, 3, 2, 1]
    assert Inseration_sort(arr.copy()) == [1, 2, 3, 4, 5], "Test case 3 failed"
    
    # Test case 4: List with duplicate elements
    arr = [3, 1, 2, 3, 1]
    assert Inseration_sort(arr.copy()) == [1, 1, 2, 3, 3], "Test case 4 failed"
    
    # Test case 5: Empty list
    arr = []
    assert Inseration_sort(arr.copy()) == [], "Test case 5 failed"
    
    # Test case 6: List with one element
    arr = [1]
    assert Inseration_sort(arr.copy()) == [1], "Test case 6 failed"
    
    # Test case 7: List with negative numbers
    arr = [3, -1, 2, -3, 0]
    assert Inseration_sort(arr.copy()) == [-3, -1, 0, 2, 3], "Test case 7 failed"
    
    print("All test cases passed")
    
if __name__ == '__main__':
    test_binseration_sort()