from faker import Faker

fake = Faker()

def contact_form_data():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "subject": fake.sentence(nb_words=3),
        "message": fake.sentence(nb_words=25)
    }
