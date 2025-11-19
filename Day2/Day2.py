class Car:
    # color = ""
    # brand = ""
    # num_seats = ""
    # Hàm khởi tạo
    def __init__(self, color, brand, num_seats):
        self.color = color
        self.brand = brand
        self.num_seats = num_seats

# car1 = Car()
# car1.brand = "Toyota"
# car1.color = "White"
# car1.num_seats = 4
# print(f"Car1 Color: {car1.color}")
# print(f"Car1 Brand: {car1.brand}")   
# print(f"Number of Seats Car1: {car1.num_seats}")

car2 = Car("Black", "Honda", 7)
print(f"Car2 Color: {car2.color}")
print(f"Car2 Brand: {car2.brand}")   
print(f"Number of Seats Car2: {car2.num_seats}")

# Chữa BT trên lớp
class VatNuoi:
    def __init__(self, ten, giong, mau_sac, can_nang):
        self.ten = ten
        self.giong = giong
        self.mau_sac = mau_sac
        self.can_nang = can_nang
    def thay_doi_thong_tin(self, ten=None, giong = None, mau_sac=None, can_nang=None):
        if ten is not None:
            self.ten = ten
        if giong is not None:
            self.giong = giong
        if mau_sac is not None:
            self.mau_sac = mau_sac
        if can_nang is not None:
            self.can_nang = can_nang
pet1 = VatNuoi("Bim", "Cho", "Vang", 10)
pet2 = VatNuoi("Mun", "Meo", "Den", 5)
pet3 = VatNuoi("Rabbit", "Tho", "Trang", 2)

print(f"Pet1: Ten: {pet1.ten}, Giong: {pet1.giong}, Mau Sac: {pet1.mau_sac}, Can Nang: {pet1.can_nang}kg")
print(f"Pet2: Ten: {pet2.ten}, Giong: {pet2.giong}, Mau Sac: {pet2.mau_sac}, Can Nang: {pet2.can_nang}kg")
print(f"Pet3: Ten: {pet3.ten}, Giong: {pet3.giong}, Mau Sac: {pet3.mau_sac}, Can Nang: {pet3.can_nang}kg")

pet1.ten = "Lu"

pet2.mau_sac = "Vang"

pet3.can_nang = 3

print(f"Pet1: Ten: {pet1.ten}, Giong: {pet1.giong}, Mau Sac: {pet1.mau_sac}, Can Nang: {pet1.can_nang}kg")
print(f"Pet2: Ten: {pet2.ten}, Giong: {pet2.giong}, Mau Sac: {pet2.mau_sac}, Can Nang: {pet2.can_nang}kg")
print(f"Pet3: Ten: {pet3.ten}, Giong: {pet3.giong}, Mau Sac: {pet3.mau_sac}, Can Nang: {pet3.can_nang}kg")

pet3.thay_doi_thong_tin(ten="Bunny", can_nang=4)

print(f"Pet3: Ten: {pet3.ten}, Giong: {pet3.giong}, Mau Sac: {pet3.mau_sac}, Can Nang: {pet3.can_nang}kg")