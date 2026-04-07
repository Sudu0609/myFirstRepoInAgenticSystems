def filter_products(products,category_name,min_price):
  result=[]

  for product in products:
    if product['category'] == category_name and product['price'] >=min_price:
      result.append(product['name'])


def filter_products(products, category_name, min_price):
    return [p['name'] for p in products 
            if p['category'] == category_name and p['price'] >= min_price]