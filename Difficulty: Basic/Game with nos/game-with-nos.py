#User function Template for python3

def game_with_number (arr,  n) : 
    #Complete the function
    l=[]
    for i in range(0,len(arr)-1):
        l.append((arr[i]^arr[i+1]))
    l.append(arr[-1])
    return l


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = game_with_number(arr, n);
    print(*res)




# } Driver Code Ends