import sys

if len(sys.argv) > 1:

    chuoi = " ".join(sys.argv[1:])
    print("Chuỗi bạn nhập là:", chuoi)
else:
    print("Vui lòng nhập chuỗi từ tham số dòng lệnh.")