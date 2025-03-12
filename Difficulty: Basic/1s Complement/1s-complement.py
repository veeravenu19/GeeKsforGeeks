#User function Template for python3
class Solution:
    def onesComplement(self,S,N):
        # code here
        int_num = int(S,2)
        s=''
        for i in range(N):
            if int_num&1<<i :
                s='0'+s
            else:
                s='1'+s
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.onesComplement(S,N))
        print("~")
# } Driver Code Ends