#  bài toán liên quan tới vòng lặp while
#  tính tổng số , đếm chữ số , số nguyên tố, số thuận nghịch
#  đếm số chữ số
n = 1234567
dem = 0
while n != 0:
    dem += 1
    n //= 10
    print("So chu so cua n:", dem)
#  tih  tổng chữ số
n = 1234
tong = 0
while n != 0:
    tong + n % 10
    n //= 10
    print("So chu so cua c:", dem)
