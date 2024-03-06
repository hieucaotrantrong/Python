# Hàm để nhập số từ người dùng
def nhap_so(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Vui lòng nhập một số hợp lệ.")

# Nhập hai số từ người dùng
a = nhap_so("Nhap so thu 1: ")
b = nhap_so("Nhap so thu 2: ")

# Lựa chọn phép toán
print("Chon phep toan:")
print("1. Cong (+)")
print("2. Tru (-)")
print("3. Nhan (*)")
print("4. Chia (/)")

chon_phep_toan = input("Lua chon: ")

if chon_phep_toan == '1':
    ket_qua = a + b
    print("Ket qua: ", ket_qua)
elif chon_phep_toan == '2':
    ket_qua = a - b
    print("Ket qua: ", ket_qua)
elif chon_phep_toan == '3':
    ket_qua = a * b
    print("Ket qua: ", ket_qua)
elif chon_phep_toan == '4':
    if b == 0:
        print("Khong the chia cho 0.")
    else:
        ket_qua = a / b
        print("Ket qua: ", ket_qua)
else:
    print("Lua chon khong hop le. Vui long chon lai.")
