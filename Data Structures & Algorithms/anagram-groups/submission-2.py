from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        g = defaultdict(list)
        for w in strs:
            g["".join(sorted(w))].append(w)
        return list(g.values())