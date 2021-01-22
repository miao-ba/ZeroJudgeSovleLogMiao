#ZeroJudge https://zerojudge.tw/ShowProblem?problemid=a006

def B4AC(a,b,c):return (b**2)-(4*a*c)#建立函式指定輸入a,b,c三值 並回傳b平方減4ac
a,b,c=map(int,input().split(" "))#輸入值以<空格>分割,再以map函式呼叫int函式分別傳回轉換為整數的分割值
if(B4AC(a,b,c)>0):print("Two different roots x1={} , x2={}".format(int((-b+B4AC(a,b,c)**0.5)/2*a),int((-b-B4AC(a,b,c)**0.5)/2*a)))#如果使用B4AC函式回傳值大於零就以格式化字串輸出方程式的兩相異解 *{}為接收後方.format()內值用
elif(B4AC(a,b,c)==0):print("Two same roots x={}".format(int((-b)/(2*a))))#如果使用B4AC函式回傳值大於零就以格式化字串輸出方程式的解
else:print("No real root")#上述兩條件皆無達成就輸出無實數解