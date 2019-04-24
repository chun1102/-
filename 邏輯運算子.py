
# ----------------------------------
x = input('請輸入身高:')
x = int(x)
y = input('請輸入性別:')

if y == '男生' and x >= 190:
    print('打籃球')
elif y == '女生' and x >= 170:
    print('打排球')

num = input('請輸入數字:')
num = int(num) % 2
if num == 0:
    print('奇數')
else:
    print('偶數')
