def maxjumps(arr):
    canreach=-1
    interval=[0,0]
    jumps=0
    if(len(arr)<=1):
        return 0
    while(True):
        jumps+=1
        for i in range(interval[0],interval[1]+1):
            canreach=max(canreach,i+arr[i])
        if(canreach>=len(arr)-1):
            return jumps
        interval[0]=interval[1]+1
        interval[1]=canreach
        if(interval[0]>interval[1]):
            return -1
print(maxjumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
        





