from faker import Faker
import string
import random

fake = Faker('pt_BR')

def random_email():
  return fake.email()

def random_cpf():
  return fake.cpf()

default_random_chars = string.ascii_letters + string.digits
def random_str(len, chars = default_random_chars):
  result_str = ''.join(random.choice(chars) for _ in range(len))
  return result_str

def randon_self_email(base_email):
  [id, domain] = base_email.split('@')
  sub_id = random_str(4)
  result_email = f'{id}+{sub_id}@{domain}'
  return result_email

def random_brazilian_phone_number():
  ddd = random_str(2, string.digits)
  first_part = random_str(5, string.digits)
  second_part = random_str(4, string.digits)
  result_phone_number = f'({ddd}) {first_part}-{second_part}'
  return result_phone_number