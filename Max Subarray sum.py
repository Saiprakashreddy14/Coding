lis = [-2, -3, 4, -1, -2, 1, 5, -3]

def maxsubarraysum(lis):
    cur_sum = lis[0]
    max_sum = lis[0]
    for i in lis[1:]:
        cur_sum=max(i,cur_sum+i)
        max_sum=max(max_sum,cur_sum)
    return max_sum
print("Max Sum is : ",maxsubarraysum(lis))


//O(n) approach using Kadanes algorithm
