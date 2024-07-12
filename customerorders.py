orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Jeff", "Une Vase", 4)
]

def print_orders():
    for order in orders:
        name, item, quantity = order
        print(f"{name} is ordering {quantity} {item}")


print_orders()

