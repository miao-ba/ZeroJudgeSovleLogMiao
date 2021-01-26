#Zerojudge 網址 https://zerojudge.tw/ShowProblem?problemid=a009

DecString = input()#輸入代解字串
for i in range(len(DecString)):print(chr(ord(DecString[i])-7),end="")#迴圈將待解字串內容依序取出再使用ord()函式將字元轉換Ascii碼減K(本題為7)再用chr()轉換為字元