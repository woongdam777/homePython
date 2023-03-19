myfile2=[]

f= open('sample02.txt','r',encoding='UTF8')

k=f.read().splitlines()
for i in k:
    elements = i.split(',')
    name = elements[0]
    age = int(elements[1])
    if age >=19:
        adult = '성인'
    else:
        adult = '미성인'
    myfile2.append(f"{name}/{age}/{adult}")

f.close()
