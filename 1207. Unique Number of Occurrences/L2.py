class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashset={}
        for i in arr:
            hashset[i]=hashset.get(i,0)+1
        if Counter(list(hashset.values()))==Counter(set(hashset.values())): #Changed len() to Counter()
            return True
        else:
            return False