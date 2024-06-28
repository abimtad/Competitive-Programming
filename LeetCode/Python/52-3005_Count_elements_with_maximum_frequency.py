class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        max_freq = max(frequency.values())
        
        total_freq = sum(freq for freq in frequency.values() if freq == max_freq)
        
        return total_freq
