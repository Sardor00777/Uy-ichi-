class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def info(self):
        return f"Mahsulot: {self.name}, Narxi: {self.price}, Qoldiq: {self.quantity}"
    
    def sell(self, amount):
        if amount > self.quantity:
            return "Xatolik: Omborda yetarli mahsulot yoq!"
        self.quantity -= amount
        return f"{amount} dona {self.name} sotildi. Qoldiq: {self.quantity}"
    
    def restock(self, amount):
        self.quantity += amount
        return f"{amount} dona {self.name} qoshildi. Yangi qoldiq: {self.quantity}"

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

    def info(self):
        data = super().info()
        data += f", garantiya: {self.warranty}yil"
        return data

class Food(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    def info(self):
        data = super().info()
        data += f", Yaroqlilik muddati: {self.expiration_date}"
        return data
    
    def sell(self, amount, current_date):
        if current_date > self.expiration_date:
            return "Xatolik: Mahsulotning yaroqlilik muddati otgan!"
        return super().sell(amount)


phone = Electronics("iPhone 13", 1000, 5, 12)
apple = Food("Olma", 2, 10, "2025-01-01")

print(phone.info())   
print(apple.info())   

print(phone.sell(2))  
print(apple.sell(5, "2024-12-01"))  

print(apple.sell(3, "2025-02-01")) 

print(phone.restock(3))  
print(apple.restock(5))  

print(phone.sell(10))  

