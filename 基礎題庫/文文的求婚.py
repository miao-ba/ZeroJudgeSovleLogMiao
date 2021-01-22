#ZeroJudge https://zerojudge.tw/ShowProblem?problemid=a004

while(True):#建立無窮迴圈
    try:Years=int(input())#輸入年份並用int()函式轉型為整數
    except:break#接收到例外就退出程式
    if((Years%4==0 and Years%100 != 0) or Years%400==0):print("閏年")#如果年份與四的餘數為零以及年份與一百的餘數不為零 亦或者 年份與四百的餘數為零 輸出"閏年"
    else:print("平年")#如果沒有達成以上條件輸出"平年"