# https://leetcode.com/problems/valid-palindrome/


# requires some knowledge of string methods to sanitize input. recursively check if first element and last element are the same and increment, decrement pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = "".join([letter.lower() for letter in s if letter.isalnum()])
        print(input)
        return self.helper(input, 0, len(input)-1)
        
    def helper(self, s: str, l, r):

        if l >= r:
            return True

        if s[l] != s[r]:
            return False

        return self.helper(s, l+1, r-1)
    
a = "0P"
b = Solution()
print(b.isPalindrome(a))
