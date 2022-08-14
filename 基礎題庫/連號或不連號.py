#https://zerojudge.tw/ShowProblem?problemid=c299


while(True):
    try:
        Imfor = list(map(lambda x:int(x),input().split(" ")))[1:]
        temp=0
        count=0
        Imfor.sort()
        for i in range(len(Imfor)):
            if(i == 0):temp=Imfor[i]
            else:
                if(Imfor[i]-temp == 1):
                    count+=1
                    temp=Imfor[i]
        if(count== len(Imfor)-1):
            print(f"{Imfor[0]} {Imfor[-1]} yes")
        else:
            print(f"{Imfor[0]} {Imfor[-1]} no")

    except:
        break