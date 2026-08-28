class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashset={}
        for i in arr:
            hashset[i]=hashset.get(i,0)+1
        if len(list(hashset.values()))==len(set(hashset.values())):
            return True
        else:
            return False