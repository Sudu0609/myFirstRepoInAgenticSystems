def filter_products(products, category_name, min_price):
    result = []
    
    for product in products:
        if product['category'] == category_name and product['price'] >= min_price:
            result.append(product['name'])
    
    return result

products = [
    {'name': 'Laptop', 'category': 'Electronics', 'price': 50000},
    {'name': 'Shirt', 'category': 'Clothing', 'price': 1500},
    {'name': 'Phone', 'category': 'Electronics', 'price': 20000}
]

result = filter_products(products, 'Electronics', 20000)
print(result)