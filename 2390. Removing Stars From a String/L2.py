class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for i in s:
            if i is '*':
                ans.pop()
            else:
                ans+=[i]#Another option (worse approach)-extends the list by adding list to a list of single element
        return ''.join(ans)