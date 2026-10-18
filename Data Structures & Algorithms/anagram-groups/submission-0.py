class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        i = 0
        a = []
        for s in strs:
            sex = "".join(sorted(s))
            if sex in d:
                pass
            else:
                d[sex] = i
                a.append([])
                i += 1
            a[d[sex]].append(s)
        return a
