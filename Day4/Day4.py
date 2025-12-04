#  Bài 1
# class Dongvat:
#     def __init__(self, ten, tuoi, loai, moi_truong_song):
#         self.ten = ten
#         self.tuoi = tuoi
#         self.loai = loai
#         self.moi_truong_song = moi_truong_song

#     def moi_truong_song_update(self, moi_truong_song_moi):
#         self.moi_truong_song = moi_truong_song_moi

#     def in_thong_tin(self):
#         print(f"Tên động vật: {self.ten}, tuổi: {self.tuoi}, loai: {self.loai}, môi trường sống: {self.moi_truong_song}")

# pet1 = Dongvat("Bim", 3, "Chó", "Nhà ông ngoại")
# print("Thông tin động vật ban đầu:")
# pet1.in_thong_tin()
# pet1.moi_truong_song_update("Nhà mình")
# print("Thông tin động vật sau khi cập nhật môi trường sống:")
# pet1.in_thong_tin()

# Bài 2
class PhuongTien:
    def __init__(self, bien_so, hang_xe, mau_sac):
        self.bien_so = bien_so
        self.hang_xe = hang_xe
        self.mau_sac = mau_sac
    def mau_sac_update(self, mau_sac_moi):
        self.mau_sac = mau_sac_moi

    def display_info(self):
        print(f"Biển số: {self.bien_so}, Hãng xe: {self.hang_xe}, Màu sắc: {self.mau_sac}") 

class Xemay(PhuongTien):
    def __init__(self, bien_so, hang_xe, mau_sac, loai_xe):
        super().__init__(bien_so, hang_xe, mau_sac)
        self.loai_xe = loai_xe

    def display_info(self):
        super().display_info()
        print(f"Loại xe: {self.loai_xe}")

class Oto(PhuongTien):
    def __init__(self, bien_so, hang_xe, mau_sac, so_cho_ngoi):
        super().__init__(bien_so, hang_xe, mau_sac)
        self.so_cho_ngoi = so_cho_ngoi

    def display_info(self):
        super().display_info()
        print(f"Số chỗ ngồi: {self.so_cho_ngoi}")

print("Thông tin phương tiện:")
pt = PhuongTien("29C-12345", "Honda", "Đỏ")
pt.display_info()
print("Thông tin phương tiện xe máy:")
bike = Xemay("29A-12345", "Honda", "Đỏ", "Xe số")
bike.display_info()
print("Thông tin phương tiện ô tô:")
car = Oto("30B-67890", "Toyota", "Xanh", 5)
car.display_info()
