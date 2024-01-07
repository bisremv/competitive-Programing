class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp=list(nums1)
        temp.extend(nums2)
        temp.sort()
        print(temp)
        median=0
        x=0
        n=len(temp)
        if n%2==0:
            x=n/2
            median=(temp[int(x-1)]+temp[int(x)])/2
        else:
            x=(n//2)+1
            median=temp[x-1]
        return median
        