coins = [1,2,20,32,56,57,34,23,67,400,200]
target = 421
dic={}

def solve(x):
    if(x<0):
        return 99999
    if(x==0):
        return 0
    if x in dic:
        return dic[x]
    best = 99999
    for i in coins:
        best = min(best,solve(x-i)+1)
    dic[x]=best
    return best

print("Best Solution is ",solve(target))
total = 0

for i in dic:
    if(dic[i]==target)
