import os.path

dic = {}

if not os.path.isfile('mydictionary.txt'):
    fo = open('mydictionary.txt','w')
    print('new file')
else:
    fo = open('mydictionary.txt','r')
    print('old file')
    
for row in fo.readlines():
    data = row.split(':')
    
    key = data[0]
    value = data[1]
    value = value.strip()
    
    dic[key]=value
    
    
    
    
    
    
    
    
    
    
    
    
while True:
    print('1.建立字彙')
    print('2.列印全部資料')
    print('3.英翻中')
    print('4.中翻英')
    print('5.學習測驗')
    print('6.離開系統')
    sel = input('請輸入功能選項:')
    if sel=='1':
        en = input('輸入英文:')
        ch = input('輸入中文:')
        dic[en]=ch
        
        
        fo = open('mydictionary.txt','w')
        for k,v in d.items():
            fo.write(k)
            fo.write(':')
            fo.write(v)
            fo.write('\n')
        fo.close()
        
    
    
    
    elif sel=='2':
        for k,v in dic.items():
            print(k,':',v)
    elif sel=='3':
        search = input('搜尋英文:')
        print(dic[search])
    elif sel=='4':
        search = input('搜尋中文:')
        for k,v in dic.items():
            if search==v:
                print(k)
    elif sel=='5':
        score=0
        for k,v in dic.items():
            print(v,':')
            ans = input('請輸入你的答案:')
            if ans==k:
                print('恭喜答對')
                score = score + 1
        print('你的分數:',score)
                
    
    
    elif sel=='6':
        break
    