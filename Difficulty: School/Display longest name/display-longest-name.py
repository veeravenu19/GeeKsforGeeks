
from typing import List


class Solution:
    def longest(self, n : int, names : List[str]) -> str:
        # code here
        a=names.copy()
        names.sort(key=len)
        for i in a:
            if len(i)==len(names[-1]):
                return i
#{ 
 # Driver Code Starts

class StringArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=input().strip().split()#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        names=StringArray().Input(n)
        
        obj = Solution()
        res = obj.longest(n, names)
        
        print(res)
        

# } Driver Code Ends