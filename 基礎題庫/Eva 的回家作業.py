#Zerojudge 網址 https://zerojudge.tw/ShowProblem?problemid=a005

TestDataNum = int(input())#輸入測試資料筆數
DataBox=[]#建立總資料串列
for i in range(TestDataNum):#以測試資料筆數'TestDataNum'為迴圈次數
    Data=list(map(int,input().split(" ")))#輸入一字串並以split()方法以空格分割字串，並用map將每個值轉型為整數並將整筆資料以list()轉換為串列給Data作為當前測資
    if(Data[1] - Data[0] == Data[2] - Data[1]):Data.append(Data[3]+(Data[2] - Data[1]))#將Data的第二筆資料減第一筆資料 比對 第三筆資料減第二筆資料 如果相等則為等差數列 並將當前測資apend進最後一筆資料加上第二筆與第一筆資料的差
    else:Data.append(int(Data[3]*(Data[1]/Data[0])))#將Data的第二筆資料除第一筆資料 比對 第三筆資料除第二筆資料 如果相等則為等比數列 並將當前測資apend進最後一筆資料乘上第二筆與第一筆資料的商數 *注意這裡使用int()再將計算結果轉型為整數
    DataBox.append(Data)#將當筆測資append進總資料串列
for i in DataBox:#將總資料串列資料以for迴圈依序取出
    for j in i: print(j,end=" ")#將當前取出測資再以for迴圈將資料依序取出並輸出再設定結尾為一個空白 *因應題目要求單行輸出
    print("")#輸出空字串換行 *因應有多筆資料換行以準備輸出下一筆資料
    