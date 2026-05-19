import csv

def get_expected_categories():
    return {'women': ['dress', 'tops', 'saree'],
            'men': ['tshirts', 'jeans'],
            'kids': ['dress', 'tops & shirts']}

def get_expected_brands():
    return ["POLO", "H&M", "MADAME", "MAST & HARBOUR", "BABYHUG", "ALLEN SOLLY JUNIOR", "KOOKIE KIDS", "BIBA"]

def get_all_products():
    products = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            products.append(row)

    return products

def get_products_count():
    products = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            products.append(row)

    return len(products)

def get_product_names():
    product_names = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            product_names.append(row["name"])

    return product_names

def get_product_prices():
    product_prices = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            product_prices.append(row["price"].replace("Rs. ", "").strip())

    return product_prices
