#APCS 2021 01 09 實作第一題
#ZeroJudge網址 https://zerojudge.tw/ShowProblem?problemid=f605

n,d=map(int,input().split(" "))#輸入商品量n(int)及接受價差d(int)
CountBuy=0#計算購買商品數量
Amount=0#購買總價
for i in range(n):#以商品量n作為迴圈次數
    x,y,z=map(int,input().split(" "))#輸入近三天商品價x,y,z
    if(max([x,y,z])-min(x,y,z)>=d):#如果x,y,z的最大值減x,y,z的最小值大於等於接受價差d
        CountBuy+=1#購買商品數量加一
        Amount+=int((x+y+z)/3)#購買總價加上近三天價格平均(轉型為整數)
print(CountBuy,Amount)#輸出購買商品數量,購買總價