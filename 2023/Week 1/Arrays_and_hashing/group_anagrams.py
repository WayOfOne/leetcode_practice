# https://leetcode.com/problems/group-anagrams/description/


# O(m * nlogn) where m is list size and n is word length
# can probably speed it up to make a dict of alphabet letters instead of sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            result["".join(sorted(word))].append(word)
        return result.values()