#UVA
#ZeroJudge網址 https://zerojudge.tw/ShowProblem?problemid=c002

while(True): #無窮迴圈
    N = int(input()) #輸入N  
    if(N!=0): #如果N不等於0
        if(N<=100):print(f"f91({N}) = 91") #N 小於等於 100 輸出 91
        else:print(f"f91({N}) = {N-10}") # N 大於 100 輸出 N -10
    else:break #等於0則退出迴圈