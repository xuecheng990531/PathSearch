f = open("/Users/lixuecheng/Desktop/good/txt/modified/network_final.txt","r")
lines = f.readlines()#读取全部内容
default='add_edge(adj,'
for line in lines:
    line=line.strip('\n')
    if line.count(',')==1:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
    elif line.count(',')==0:
        print((default+line+','+line+')'))
    elif line.count(',')==2:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
    elif line.count(',')==3:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
    elif line.count(',')==4:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
    elif line.count(',')==5:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
    elif line.count(',')==6:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
        print(default+line.split(',')[0]+','+line.split(',')[6]+')')
    elif line.count(',')==7:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
        print(default+line.split(',')[0]+','+line.split(',')[6]+')')
        print(default+line.split(',')[0]+','+line.split(',')[7]+')')
    elif line.count(',')==8:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
        print(default+line.split(',')[0]+','+line.split(',')[6]+')')
        print(default+line.split(',')[0]+','+line.split(',')[7]+')')
        print(default+line.split(',')[0]+','+line.split(',')[8]+')')
    elif line.count(',')==10:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
        print(default+line.split(',')[0]+','+line.split(',')[6]+')')
        print(default+line.split(',')[0]+','+line.split(',')[7]+')')
        print(default+line.split(',')[0]+','+line.split(',')[8]+')')
        print(default+line.split(',')[0]+','+line.split(',')[9]+')')
        print(default+line.split(',')[0]+','+line.split(',')[10]+')')
    elif line.count(',')==9:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
        print(default+line.split(',')[0]+','+line.split(',')[6]+')')
        print(default+line.split(',')[0]+','+line.split(',')[7]+')')
        print(default+line.split(',')[0]+','+line.split(',')[8]+')')
        print(default+line.split(',')[0]+','+line.split(',')[9]+')')
    elif line.count(',')==11:
        print(default+line.split(',')[0]+','+line.split(',')[1]+')')
        print(default+line.split(',')[0]+','+line.split(',')[2]+')')
        print(default+line.split(',')[0]+','+line.split(',')[3]+')')
        print(default+line.split(',')[0]+','+line.split(',')[4]+')')
        print(default+line.split(',')[0]+','+line.split(',')[5]+')')
        print(default+line.split(',')[0]+','+line.split(',')[6]+')')
        print(default+line.split(',')[0]+','+line.split(',')[7]+')')
        print(default+line.split(',')[0]+','+line.split(',')[8]+')')
        print(default+line.split(',')[0]+','+line.split(',')[9]+')')
        print(default+line.split(',')[0]+','+line.split(',')[10]+')')
        print(default+line.split(',')[0]+','+line.split(',')[11]+')')