#Zerojudge 網址 https://zerojudge.tw/ShowProblem?problemid=a010

FixNum = int(input())#輸入待分解數字
NumDict={}#建立因數字典
OutSring=""#建立輸出字串
while(True):#執行無窮迴圈
    for i in range(2,FixNum+1):#以待分解數字為次數執行for迴圈
        if (FixNum%i==0):#如果待分解數字可被當次的i整除
            FixNum = int(FixNum/i)#將待分解分數除以i *這裡要把結果再轉型為整數，否則執行下次迴圈時將無法成功建立range
            if(NumDict.get(i)!=None):#如果用get取得因數字典裡i為索引值的值 如果取得值不為None
                NumDict[i]+=1#因數字典內以i為索引值資料的值加一
            else:#如果以i為索引值的資料不存在
                NumDict[i]=1#建立以i為索引值的資料並預設值為1
            break#結束當次for迴圈
    if(FixNum == 1):#如果FixNum為1
        break#結束While無窮迴圈
for i,j in NumDict.items():#用.item()字典方法取得字典索引值(key)以及值(value)
    if(j!=1):#如果該項資料值不只有1
        OutSring+=f"{i}^{j}"#輸出字串加上f-string(字串前加f可在{}內轉寫程式片段並自動轉型為字串)
    else:#如果該項資料值只有1
        OutSring+=str(i)#輸出字串加上該項資料索引值(因數)
    OutSring+=" * "#輸出字串加上<空格>*空格
print(OutSring[:-3])#輸出使用分割字串[字串第幾個位置(整數):(到)字串第幾個位置(整數)]輸出 *由於最後會多出一個" * "所以輸出到倒數第四個字元[:-3]