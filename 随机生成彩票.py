import random
temp=[x for x in range(1,34)]
temp1=[x for x in range(1,17)]
n=int(input('请输入你想选的组数：'))
k=1
while k <=n:
    random.shuffle(temp)
    random.shuffle(temp1)
    slit=random.sample(temp,6)
    slit.sort()
    slit1=random.sample(temp1,1)
    print(slit+slit1)
    k+=1

