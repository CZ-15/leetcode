class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        left = right = max_length = 0
        for right in range(len(s)):
            while s[right] in s_set:
                s_set.remove(s[left])
                left += 1
            s_set.add(s[right])
            length = len(s_set)
            max_length = max(length, max_length)
        return max_length
            

            