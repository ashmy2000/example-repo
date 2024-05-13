class House():
    def __init__(self, address, area,price):
        # instance variable as it has self in-front
        self.address = address
        self.area = area
        self.price = price

        # class variable
        House.quality = "Low"
        # instance variable
        self.quality = "Medium"
        # Local variable
        quality = "High"

soho_house = House("Wolvo", 52, 300000)
print(soho_house.quality)
print(House.quality)
# Can't access Local variable
soho_house.quality = "new"
print(soho_house.quality)