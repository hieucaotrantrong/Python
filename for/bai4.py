# bài tập
# bạn hãy nhập một số nguyên x bạn vừa nhập ở bàn phím .dòng 2 in ra hiếu dòng 3 in ra phương
a = int(input())
print(a)
print("Hieu")
print("Phuong")
#  vòng lặp trong python
# vòng lặp for
# cú pháp range()
a = range(1, 20, 2)
for i in a:
    print(i, end=" ")
# #   luôn duyệt các số từ 1 tới 30
for i in range(1, 31, 1):
    print(i, end=" ")
    for i in range(10):
        print(i, "Hieu yeu phuong")
# #   vd  tính tổng  dãy số vd S(n)=1+2+3+...+n
n = 20
S = 0
for i in range(1, n + 1):
    S += i
    print(S)
# in ra các số cho 1 tới 30, nhưng gặp số nào chia hết cho 8 thì duwngg lại
for i in range(1, 21):
    print(i, end="")
    if i % 7 == 0:
        break
print("bạn đã hoàn thành vòng lặp")
# câu lệnh continue câu lệnh sẽ quay trở lại khi gặp continue
for i in range(5):
    print("28 tech")
    continue
print("python")
# for lồng nhau
for i in range(3):
    for j in range(2):
        print(i, j)
