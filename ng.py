import random
# 設定範圍
r_start = input('請輸入最小值')
r_end = input('請輸入最大值')
r_start = int(r_start)
r_end = int(r_end)
while True:
    if r_start >= r_end:
        print('最小值一定要小於最大值喔！')
        r_start = str(r_start)
        r_start = input('請重新輸入最小值')
        r_start = int(r_start)
        r_end = str(r_end)
        r_end = input('請重新輸入最大值')
        r_end = int(r_end)
    else:
        break

# 正式遊戲
print('數字範圍設定成功，遊戲正式開始')
rn = random.randint(r_start, r_end)
rg = input('猜猜數字是多少？')
rg = int(rg)
nt = 1
count = print('你已經猜', nt, '次了喔！')

while True:
    if rg > r_end or rg < r_start:
        print('請輸入',r_start, '到',r_end, '的數字喔！')
        rg = input('再猜一次?')
        rg = int(rg)
    if rn > rg:
        print('再猜大一點')
        rg = input('再猜一次?')
        rg = int(rg)
    elif rn < rg:
        print('再猜小一點')
        rg = input('再猜一次?')
        rg = int(rg)
    else:
        print('恭喜猜對了！')
        print('你總共猜了', nt, '次')
        break
    nt += 1
    count = print('你已經猜', nt, '次了喔！')