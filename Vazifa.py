# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
    
#     def info(self):
#         return f"Mahsulot: {self.name}, Narxi: {self.price}, Qoldiq: {self.quantity}"
    
#     def sell(self, amount):
#         if amount > self.quantity:
#             return "Xatolik: Omborda yetarli mahsulot yoq!"
#         self.quantity -= amount
#         return f"{amount} dona {self.name} sotildi. Qoldiq: {self.quantity}"
    
#     def restock(self, amount):
#         self.quantity += amount
#         return f"{amount} dona {self.name} qoshildi. Yangi qoldiq: {self.quantity}"

# class Electronics(Product):
#     def __init__(self, name, price, quantity, warranty):
#         super().__init__(name, price, quantity)
#         self.warranty = warranty

#     def info(self):
#         data = super().info()
#         data += f", garantiya: {self.warranty}yil"
#         return data

# class Food(Product):
#     def __init__(self, name, price, quantity, expiration_date):
#         super().__init__(name, price, quantity)
#         self.expiration_date = expiration_date
    
#     def info(self):
#         data = super().info()
#         data += f", Yaroqlilik muddati: {self.expiration_date}"
#         return data
    
#     def sell(self, amount, current_date):
#         if current_date > self.expiration_date:
#             return "Xatolik: Mahsulotning yaroqlilik muddati otgan!"
#         return super().sell(amount)


# phone = Electronics("iPhone 17", 1000, 5, 8)
# apple = Food("Olma", 2, 10, "2025-01-01")

# print(phone.info())   
# print(apple.info())   

# print(phone.sell(2))  
# print(apple.sell(5, "2024-12-01"))  

# print(apple.sell(3, "2025-02-01")) 

# print(phone.restock(3))  
# print(apple.restock(5))  

# print(phone.sell(10))  



  
"uyga vazifa"
from uuid import uuid4

class Basket:
    def __init__(self):
        self.__id  = uuid4
        self.products = []
        self.products2 = []

    def add(self, product, price, quantity):
        self.products.append({"product": product, "price": price, "quantity": quantity})
        return f"{product}, {quantity} savatga qo'shildi"

    def get_id(self):
        return self.__id

    def show(self): 
        if not self.products:
            return "Savat bo'sh"
        result = "Savat ichida:\n"
        for i in self.products:
            result += f"- {i['product']}: {i['price']} USD ({i['quantity']} dona)\n"
        return result

    def get_id(self):
        return self.__id

    def calc(self):
        summa = 0
        for i in self.products:
            summa += i["price"] * i["quantity"]
        return f"Umumiy narx: {summa} USD"

    def get_id(self):
        return self.__id
    def remove(self, product, quantity=1):
        for i in self.products:
            if i["product"] == product:
                if i["quantity"] > quantity:
                    i["quantity"] -= quantity
                else:
                    self.products.remove(i)
                return f"{product} ({quantity} dona) savatdan olib tashlandi"
        return f"{product} savatda topilmadi"
    

    def most_expensive(self):
        if not self.products:
            return "Savat bo'sh"
        max_product = max(self.products, key=lambda x: x["price"])
        return f"Eng qimmat mahsulot: {max_product['product']} - {max_product['price']} USD"

    def delete_basket(self):
        self.products.clear() 
        return "Savat butunlay bo'shatildi!"


b=Basket()
print(b.add("Apple", 2, 2))
print(b.add("Mackbook", 3, 3))
print(b.most_expensive())
print(b.delete_basket())
