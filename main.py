item = "chai"
price = 15
try:
    quantity = int(input("Quantity bataye :"))
except ValueError:
    print("sahi number dalo")
    exit()
total = price * quantity
if total >= 100:
    discount = total * 10 / 100
else:
    discount = 0
final = total - discount
print(f"item:{item} | price:{price} | qty:{quantity} | Total:{total} | Discount:{discount} | Final:{final}")