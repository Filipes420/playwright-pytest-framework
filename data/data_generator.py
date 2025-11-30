from faker import Faker
import csv
import random

fake = Faker()

def create_contact_form_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "subject": fake.sentence(nb_words=3),
        "message": fake.sentence(nb_words=25)
    }

def get_random_product():
    products = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            products.append(row)

    return random.choice(products)

def get_random_product_word():
    products = []

    with open("data/products_data.csv", "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            products.append(row)

    random_product = random.choice(products)
    random_product = random_product[0]
    words = random_product.split(" ")
    return random.choice(words)



