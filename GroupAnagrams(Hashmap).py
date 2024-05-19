from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list) #every non-existing key will be assgined a empty list
        for s in strs:
            count = [0] * 26 #count of all letters in s
            for c in s:
                count[ord(c) - ord("a")] += 1 #ascii code c - ascii code a, to get a list beginning at index 0
            result[tuple(count)].append(s) #store count at an index in result, if a string has the same count, it will append 
        return result.values()
