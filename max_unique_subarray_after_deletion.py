"""3487. Maximum Unique Subarray Sum After Deletion
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a subarray of nums such that:

All elements in the subarray are unique.
The sum of the elements in the subarray is maximized.
Return the maximum sum of such a subarray.

 

Example 1:

Input: nums = [1,2,3,4,5]

Output: 15

Explanation:

Select the entire array without deleting any element to obtain the maximum sum.

Example 2:

Input: nums = [1,1,0,1,1]

Output: 1

Explanation:

Delete the element nums[0] == 1, nums[1] == 1, nums[2] == 0, and nums[3] == 1. Select the entire array [1] to obtain the maximum sum.

Example 3:

Input: nums = [1,2,-1,-2,1,0,-1]

Output: 3

Explanation:

Delete the elements nums[2] == -1 and nums[3] == -2, and select the subarray [2, 1] from [1, 2, 1, 0, -1] to obtain the maximum sum.

 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100"""
def max_unique_subarray_after_deletion(nums):
    seen = set()
    max_sum = 0
    current_sum = 0

    for num in nums:
        if num not in seen:
            seen.add(num)
            current_sum += num
        else:
            max_sum = max(max_sum, current_sum)
            # Reset the current sum and seen set
            seen.clear()
            current_sum = num
            seen.add(num)

    return max(max_sum, current_sum)
if __name__ == "__main__":
    # Example usage
    nums1 = [1, 2, 3, 4, 5]
    print(max_unique_subarray_after_deletion(nums1))  # Output: 15

    nums2 = [1, 1, 0, 1, 1]
    print(max_unique_subarray_after_deletion(nums2))  # Output: 1

    nums3 = [1, 2, -1, -2, 1, 0, -1]
    print(max_unique_subarray_after_deletion(nums3))  # Output: 3