from uuid import uuid4 as id

class Basket:
    def __init__(self):
        self.products = []

    def add(self, product, price, quantity):
        product_id = id()  
        self.products.append({"product": product, "price": price, "quantity": quantity, "id": product_id})
        return f"Mahsulot: {product}, soni: {quantity}, id: {product_id} savatga qo'shildi"

    def show(self): 
        if not self.products:
            return "Savat bo'sh"
        result = "Savat ichida:\n"
        for i in self.products:
            result += f"- {i['product']} (ID: {i['id']}): {i['price']} USD ({i['quantity']} dona)\n"
        return result

    def calc(self):
        summa = sum(i["price"] * i["quantity"] for i in self.products)
        return f"Umumiy narx: {summa} USD"

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


b = Basket()
print(b.add("Apple", 2, 2))
print(b.add("MacBook", 3000, 1))
print(b.add("Phone", 1000, 1))
print(b.show())
print(b.most_expensive())
print(b.delete_basket())
