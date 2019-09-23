import random

rn = random.randint(1, 100)
rg = input("猜猜數字是多少？")
rg = int(rg)
nt = 1

while True:
    if rn > rg:
        print("再猜大一點")
        rg = input("再猜一次")
        rg = int(rg)
        nt = nt + 1
    elif rn < rg:
        print("再猜小一點")
        rg = input("再猜一次")
        rg = int(rg)
        nt = nt + 1
    else:
        print("恭喜猜對了！")
        print('你總共猜了', nt, '次')
        break