#https://zerojudge.tw/ShowProblem?problemid=b516

t = lambda x:chr(ord(x)+3)
l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W"]
DeMap= {}
for i in l:DeMap[i]=t(i)
DeMap["X"],DeMap["Y"],DeMap["Z"] = "A","B","C"
s = int(input())
for i in range(s):
    a = input()
    b = ''
    for j in a:
        b += DeMap[j] 
    print(b)