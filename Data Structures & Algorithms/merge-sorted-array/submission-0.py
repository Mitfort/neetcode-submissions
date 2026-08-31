class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            nums1[:] = nums2
            return 
        
        ptr1 = m - 1
        ptr2 = n - 1

        p = m + n - 1

        while ptr2 >= 0:
            if ptr1 >= 0 and nums1[ptr1] > nums2[ptr2]:
                nums1[p] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[p] = nums2[ptr2]
                ptr2 -= 1
            
            p-=1