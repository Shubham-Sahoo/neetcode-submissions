class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ss = [[] for i in range(len(nums))]
        buc = {}
        for x in nums:
            buc[x] = buc.get(x,0) + 1
        
        print(buc)
        for x in buc:
            # print(buc[x], ss)
            ss[buc[x]-1].append(x)
        
        print(ss)
        res = []
        j = len(nums)-1
        while k>0 and j>=0:
            if ss[j] != []:
                res.extend(ss[j])
                k -= len(ss[j])
            j-= 1
        
        print(res)
        return res