products = {}

while True:
    entry = input("Enter product name and price (or 'done' to finish): ")
    if entry.lower() == 'done':
        break
    try:
        name, price = entry.rsplit(' ', 1)
        products[name] = float(price)
    except ValueError:
        print("Invalid input. Please enter in the format: product price")

while True:
    query = input("Enter product name to check price (or 'exit' to quit): ")
    if query.lower() == 'exit':
        break
    print(f"Price: {products.get(query, 'Product not found')}")