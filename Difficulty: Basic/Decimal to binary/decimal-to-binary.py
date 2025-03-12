
import math
class Solution:
    def decToBinary(self, n):
        # code here
        if n==0:
            return 0
        s=''
        le = int(math.log2(n)+1)
        for i in range(le):
            if n&1<<i:
                s='1'+s
            else:
                s='0'+s
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    solution = Solution()

    for _ in range(t):
        n = int(input())
        print(solution.decToBinary(n))
        print("~")

# } Driver Code Ends