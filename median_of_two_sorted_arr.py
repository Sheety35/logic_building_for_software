class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        j = 0
        i=0
        q = []
        while(i<m and j<n):
            if nums1[i]<nums2[j]:
                q.append(nums1[i])
                i+= 1
            else:
                q.append(nums2[j])
                j+= 1
        while i < m:
            q.append(nums1[i])
            i +=1
        while j < n:
            q.append(nums2[j])
            j +=1
        a = len(q)//2
        if len(q) % 2 == 0:
            val = (q[a] + q[a - 1]) / 2
        else: 
            val = q[a]
        return val