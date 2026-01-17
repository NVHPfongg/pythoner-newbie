# Bai 1: Tong cac so thoa dieu kien

# De bai: Nhap vao mot so nguyen duong n la so luong so can nhap vao
# Tinh tong cac so chia het cho 3 nhung khong chia het cho 5 trong khoang tu 1 den n

n = int(input("nhap vao so n:"))
sum = 0
for i in range(0,n+1):
    if i % 3 == 0 and i % 5 != 0:
        sum += i

print(sum)
# Bai 2: Dem chu so cua mot so nguyen
# De bai: Nhap vao mot so nguyen duong n. Hay dem xem n co bao nhieu chu so

n = int(input("nhap vao n:"))
dem = 0

while n > 0:
    dem += 1
    n //=10
    print(n)
print(dem)
# Bai 3: Kiem tra so nguyen to
# De bai: Nhap vao mot so ng"uyen duong n. Kiem tra xem n co phai la mot so nguyen to hay khong
n = int(input("nhap vao so n:"))
for i in range(1,n+1):
    if n % i == 0:
        dem +=1

if dem == 2:
    print("la so nguyen to")
else:
    print("khong phai la so nguyen to")