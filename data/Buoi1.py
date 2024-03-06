""" ví dụ chúng ta có biến a khởi tạo giá trị cho nó là 100 chúng ta in ra python sẽ tự hiển thị kiểu dữ liệu gì
"""
a=100
b=100
c="hello "
print(type(a,))
# không được đặt tên biến có dấu cách kí tự đặc biệt bắt đầu bẵng chữ hoặc bằng số vd
# dien tich=100
print("dien tich")
#  kiểu dữ liệu số trong python
a=50
b=50.0
c=100-50j
print('kieu du lieu cua bien a ',type(a))# đây là kiểu dữ liệu số nguyên
print('kieu du lieu cua bien b',type(b))# đây là kiểu dữ liệu số thực dấu phẩy cộng
print(' kieu du lieu cua bien c',type(c)) # đây là kiểu dữ liệu số phứcnó được hiểu là có một chữ sau một con số thì sẽ là số phức
# # máy tính nó hiểu khác nhau về số nguyên và số thực tuy nó giống nhau
#kiểu dữ liệu số  phức
# in số thực với số lượng chữ số sau dấu phẩy xác định
a=10.1181818181
print('%.2f'% a)
print('{:.2f}'.format(a))
# in số phức phần thực ra phần thực phần ảo ra phẩn ảo
a=3+5j
print(a.real)
print(a.imag)
# kiểu dữ liệu đúng sai
a= True
print(bool(a))
b="hieu dep trai"
print(bool(b))
# xâu kí tự trong python
s="hieudeptrai"
print(type(s))
#  xâu nhiều kí tự trong python
s='''hieu dep trai
hieu rat dep trai
hieu yeu phuongg'''
print(s)
print(type(s))
# kiểu dữ liệu ép kiểu
a=10.3534
a= int(a)
print(type(a))
print(a)