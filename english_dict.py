d={}
print('歡迎來到英文系統')
while True:
    print('1.建立辭典')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    option=input('輸入選項:')
    if option=='6':
        break
    elif option=='1':
        while True:
            voc=input('輸入新單字(按0離開)')
            if voc=='0':
                break
            if voc not in d:
                voc_ch=input('中文:')
                d[voc]=voc_ch
            else:
                print('存在')
    elif option=='2':
        s=sorted(d)
        print(s)
        for i in s:
            print(i,':',d[i])
    elif option=='3':
        voc=input('輸入英文(按0離開)')
        
        if voc=='0':
            break
        if voc in d:
            print(voc,'中文是',d[voc])
        else:
            print('沒有這個單字')
    elif option=='4':
        while True:
            got=False
            ch=input('輸入中文(按0離開)')
            if ch=='0':
                break
            for k,v in d.items():
                if ch==v:
                    print(ch,'的英文是',k)
                    got=True
                    
            if got==False:
                print('沒有這個單字')
    elif option=='5':
        score=0
        for k,v in d.items():
            print(v,':')
            ans=input()
            if ans==k:
                score+=1
                print('答對了')
                
            else:
                print('答錯了')
        print('得',score,'分')
            
            
            
 





               