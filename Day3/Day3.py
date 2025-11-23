class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
# Phương thức không có giá trị trả về
    def info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
# Phương thức có giá trị trả về

    def discount_price(self, discount):
        return self.price * (1 - discount / 100)

phone1 = Phone("Apple", "iPhone 13", 500)
phone2 = Phone("Samsung", "Galaxy S23", 400)

phone1.info()
print("Discounted Price (10%):", phone1.discount_price(10))
phone2.info()
print("Discounted Price (15%):", phone2.discount_price(15))

class PhuongTien:
    def __init__(self, loai_xe, hang_xe, mau_sac, so_cho, so_banh_xe, gia_tien):
        self.loai_xe = loai_xe
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
        self.so_cho = so_cho
        self.so_banh_xe = so_banh_xe
        self.gia_tien = gia_tien
    def thong_tin_xe(self):
        print("Loại xe:", self.loai_xe)
        print("Hãng xe:", self.hang_xe)
        print("Màu sắc:", self.mau_sac)
        print("Số chỗ:", self.so_cho)
        print("Số bánh xe:", self.so_banh_xe)
        print("Giá tiền:", self.gia_tien)

    def gia_ban_giam_gia(self, giam_gia):
        return self.gia_tien * (1 - giam_gia / 100)


xe1 = PhuongTien("Ô tô", "Toyota", "Đỏ", 5, 4, 30000)
xe1.thong_tin_xe()
print("Giá bán sau giảm giá (10%):", xe1.gia_ban_giam_gia(10))

# Kế thừa trong Python

class Xe:
    def __init__(self, hang, mau, gia):
        self.hang = hang
        self.mau = mau
        self.gia = gia
    
    def khoi_dong(self):
        print(f"Xe {self.hang} đang khởi động...")   

# Class con

class XeDap(Xe):
    def dap_bang_hai_banh(self):
        print(f"Xe {self.hang} đang được đạp về phái trước.")

class XeHoi(Xe):
    def chay_bang_bon_banh(self):
        print(f"Xe {self.hang} đang chạy về phía trước bằng dộng cơ.")



class Xemay(PhuongTien):
    def __init__(self, loai_xe, hang_xe, mau_sac, so_cho, so_banh_xe, gia_tien, toc_do):
        super().__init__(loai_xe, hang_xe, mau_sac, so_cho, so_banh_xe, gia_tien)
        self.toc_do = toc_do

    def thong_tin_xe(self):
        super().thong_tin_xe()
        print("Tốc độ:", self.toc_do)
    
    def khoi_dong(self):
        print("Xe máy đang khởi động...")

class XeOto(PhuongTien):
    def __init__(self, loai_xe, hang_xe, mau_sac, so_cho, so_banh_xe, gia_tien, toc_do):
        super().__init__(loai_xe, hang_xe, mau_sac, so_cho, so_banh_xe, gia_tien)
        self.toc_do = toc_do

    def thong_tin_xe(self):
        super().thong_tin_xe()
        print("Tốc độ:", self.toc_do)
    
    def khoi_dong(self):
        print("Xe ô tô đang khởi động...")
    
    def mo_cua_so(self):
        print("Cửa sổ xe ô tô đang mở...")
