#APCS 2022 06 13 實作第一題
#ZeroJudge網址 https://zerojudge.tw/ShowProblem?problemid=i399

A = list(map(lambda x:int(x),input().split(" ")))
B= []
pin = 0
count = 0
for i in range(len(A)):
    temp = 0
    for j in range(len(A)):
        if(A[i]==A[j]):temp+=1
    if (temp > count):
        pin = i
        count =temp
for i in A:
    if(i not in B):B.append(i)
B.sort(reverse=True)
print(count,end=" ")
for i in B:print(i,end=" ")