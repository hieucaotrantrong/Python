# break
a = 5
b = 1
while b <= a:
    print(b)
    if b == 3:
        break
    b += 1
    # yêu cầu nhập số dương , nhập số âm hoặc số 0 nhập lại
while True:
    a = int(input("Nhap a :"))
    if a == 100:
        break
