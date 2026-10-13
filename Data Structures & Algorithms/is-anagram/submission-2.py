class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first_dic = {}
        #for c in s:
            #if first_dic[c] == 0:
                #first_dic[c] == 
        if len(s) != len(t):
            return False
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True