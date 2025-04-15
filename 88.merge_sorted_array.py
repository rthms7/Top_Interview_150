# Intuition
#<!-- Handle edge case of empty nums1. While nums2 still has values compare traverse nums1 and compare with first element of nums2. if nums2 element is less than then pop and append it before element under consideration in nums1. Avoid duplicates in nums 1 by increasing the index andappend remaining elements of nums2 when end of nums1 is reached. Use append and pop since nums1 needs to be modified in place. Intuition code between 0 and 1 ms time -->

# Alternate approach
#<!-- start overwriting elements in nums1 from end of list at index m+n-1. advantage: no special handling of edge cases-->
'''
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
	a, b, write_index = m-1, n-1, m + n - 1

	while b >= 0:
		if a >= 0 and nums1[a] > nums2[b]:
			nums1[write_index] = nums1[a]
			a -= 1
		else:
			nums1[write_index] = nums2[b]
			b -= 1

		write_index -= 1
'''

# Complexity
#- Time complexity: O(M+N)


#- Space complexity: O(1)


# Code
#```python []

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m:
            nums1.pop()
        #print(nums1)
        nums2 = nums2[:n]

        if nums2 and not nums1:
            [nums1.append(i) for i in nums2]
            return None
 
        i = 0
        while nums2:
            #print(nums1, nums2)
            #print(i)
            if nums2[0] <= nums1[i]:
                nums1.insert(i,nums2.pop(0))
                i += 1
                continue
            if i < len(nums1)-2 and nums1[i] == nums1[i+1]:
                i += 1
                continue
            if i == len(nums1)-1:
                [nums1.append(i) for i in nums2]
                break
            i += 1
            