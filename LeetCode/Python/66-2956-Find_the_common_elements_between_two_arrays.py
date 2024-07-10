class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_nums2 = set(nums2)
        set_nums1 = set(nums1)

        answer1 = sum(1 for num in nums1 if num in set_nums2)
        answer2 = sum(1 for num in nums2 if num in set_nums1)

        return [answer1, answer2]
