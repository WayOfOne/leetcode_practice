# https://leetcode.com/problems/group-anagrams/description/


# O(m * nlogn) where m is list size and n is word length
# can probably speed it up to make a dict of alphabet letters instead of sorting
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            result["".join(sorted(word))].append(word)
        return result.values()
    
# O(m * n) where m is list size and n is word length
# use a tuple of counts of each letter instead of sorting
# we have to use a tuple because lists and dictionaries are not hashable so they can't be used as keys
# in python this cause a TypeError: unhashable type: 'list' but in C# it would be a compile time error
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            result[tuple(count)].append(word)
        return result.values()
    
    