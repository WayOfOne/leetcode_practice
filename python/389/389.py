from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_letters = Counter([a for a in s])

        for letter in t:
            if s_letters.get(letter,0) > 0:
                s_letters.subtract(letter)
            else:
                return letter
        

if __name__ == "__main__":
    a = Solution()
    print(a.findTheDifference('aaa','aaab') == 'b')
