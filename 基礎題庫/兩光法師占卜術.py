#Zerojudge 網址 https://zerojudge.tw/ShowProblem?problemid=a003

IsLuckList=["普通","吉","大吉"]#建立一串列利用串列索引值特性分別為0,1,2分別定義值為"普通","吉","大吉"
M,D = map(int,input().split(" "))#輸入值以<空格>分割,再以map函式呼叫int函式分別傳回分割值
print(IsLuckList[(M*2+D)%3])#以M的兩倍加D的三的餘數作為串列IsLuckList的索引值
