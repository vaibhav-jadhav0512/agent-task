Here's a Python solution for finding the median of two sorted arrays that meets all the requirements specified:

```python
from typing import List

def median_of_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Find the median of two sorted arrays.

    Parameters:
    - nums1 (List[int]): The first sorted array.
    - nums2 (List[int]): The second sorted array.

    Returns:
    - float: The median of the two sorted arrays.

    Example usage:
    >>> median_of_sorted_arrays([1, 3], [2])
    2.0
    >>> median_of_sorted_arrays([1, 2], [3, 4])
    2.5
    """
    # Ensure nums1 is the smaller array to optimize the binary search
    if len(nums1) > len(nums2):
        return median_of_sorted_arrays(nums2, nums1)

    x, y = len(nums1), len(nums2)
    low, high = 0, x

    while low <= high:
        partitionX = (low + high) // 2
        partitionY = (x + y + 1) // 2 - partitionX

        maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        minX = float('inf') if partitionX == x else nums1[partitionX]

        maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        minY = float('inf') if partitionY == y else nums2[partitionY]

        if maxX <= minY and maxY <= minX:
            # Correct partitioning
            if (x + y) % 2 == 0:
                return (max(maxX, maxY) + min(minX, minY)) / 2.0
            else:
                return max(maxX, maxY)
        elif maxX > minY:
            # Move the partition to the left in nums1
            high = partitionX - 1
        else:
            # Move the partition to the right in nums1
            low = partitionX + 1

# Example usage
if __name__ == "__main__":
    print(median_of_sorted_arrays([1, 3], [2]))  # Output: 2.0
    print(median_of_sorted_arrays([1, 2], [3, 4]))  # Output: 2.5
```

### Explanation:
- **Binary Search Approach**: The function uses binary search to find the correct partition points in both arrays such that the left half contains the smaller elements and the right half contains the larger elements.
- **Optimization**: By ensuring `nums1` is the smaller array, we reduce the search space and simplify the logic.
- **Time Complexity**: The time complexity of this approach is O(log(min(m, n))), which meets the requirement.

This solution should work efficiently for the given constraints.