# Example for 'if'
a, b = 9, 10
if a > b:
    print(a)
else:
    print(b)
    print(a) if a > b else print(b)
# if...elif...else
mark = float(input("Please input your mark: "))
if 9 <= mark <= 10:
    print(f"Ecellent")
elif 8 <= mark:
    print(f"good")
elif 7 <= mark:
    print(f"Normal")
else:
    print(f"Fail")

#
tong = 0

for i in range(1, 100, 2):
    tong += i

print("Tổng các số lẻ từ 1 đến 99 là:", tong)
