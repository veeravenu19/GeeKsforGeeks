#User function Template for python3
import math

class Solution:
    def findPosition(self, n):
        # code here 
        if n==0:
            return -1
        elif n&(n-1)==0:
            le = int(math.log2(n)+1)
            for i in range(le):
                if n&(1<<i):
                    return i+1
                    
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.findPosition(N))

# } Driver Code Ends