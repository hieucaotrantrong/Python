#  toán tử gán trong pyhon
a = 100
b = a
print(a)
print(b)
# toán tử toán học python
a = 100
b = 200
Tong = a + b
print(Tong)
# toán tử so sánh
a = 100
b = 200
ra = a == b
print(ra)
print(100 < 200)
# toán tử so sánh
# toán tử logic
x = 30
print(x > 29) or (x < 100)
# toán tử nhận dạng
a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)
print(id(a))
print(id(b))
#  toán tử thành viên
a = "caotrantronghieu.java.linnux.window"
print("jaa" in a)
a = 10.1181818181
print("%.2f" % a)
print("{:.2f}".format(a))
# #  nhập dữ liệu từ bán phím trong python
a = input("Xin hay dien ten vao day:")
b = print("Ten bat ki vua nhap la")
print("hieu")
# bài toán tính hình chữ nhật trong python
a = int(input("Nhap chieu rong"))
b = int(input("Nhap chieu dai"))
chuvi = 2 * (a + b)
dientich = a * b
print(chuvi, dientich)
#  nhập số
a = input("Nhập 3 số:")
# bước 2 tách các số ra
b = a.split()
#  buowsc3 sử dụng hàm map để ép các phần tử trong list_> sang kiểu dữ liệu mong muôn
x, y, z = map(int, b)
print(x + y + z)
