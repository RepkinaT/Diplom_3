import string
from random import choice


class RandomData:
    @staticmethod
    def generate_random_name():
        first_names = ["John", "Jane", "Alex", "Emma", "Michael", "Olivia", "David", "Sophia"]
        last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson"]

        random_first_name = choice(first_names)
        random_last_name = choice(last_names)

        return f"{random_first_name} {random_last_name}"

    @staticmethod
    def generate_random_email():
        domains = ['example.com', 'ya.ru', "gmail.com", "mail.ru"]
        random_name = ''.join(choice(string.ascii_lowercase) for _ in range(8))
        random_domain = choice(domains)
        return f"{random_name}@{random_domain}"

    @staticmethod
    def generate_random_password(length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(choice(characters) for _ in range(length))
