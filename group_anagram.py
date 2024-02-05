from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_set = []
        anagram_map = defaultdict(list)
        for str in strs:
            sorted_str = tuple(sorted(str))
            anagram_map[sorted_str].append(str)
        for word in anagram_map.values():
            result_set.append(word)
        return result_set