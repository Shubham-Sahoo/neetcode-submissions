class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            x = "".join(sorted(s))
            if x in res:
                res[x].append(s)
            else:
                res[x] = [s]
        
        # print(res)
        result = []
        for x in res:
            result.append(res[x])
        
        return result