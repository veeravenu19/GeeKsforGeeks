#User function Template for python3
class Solution:
    def revStr (self, s : str) -> str :
        # code here 
        c=s[::-1]
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        
        ob = Solution()
        print(ob.revStr(s))
# } Driver Code Ends