#User function Template for python3
import math
class Solution:
    def isBitSet (self, N):
        
        if N==0:
            return 0
        
        le = int(math.log2(N))
        for i in range(le):
            if N & (1<<i) == 0:
                return 0
        return 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isBitSet(N))
        print("~")
# } Driver Code Ends