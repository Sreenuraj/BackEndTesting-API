from datetime import datetime
import string
import random


def generate_random_info():
    info = {}
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # generate random email and user_name
    info['email'] = 'api_user_'+stamp+'@gmail.com'
    info['user_name'] = 'backend'+stamp

    # generate random first_name and last_name
    all_letters = string.ascii_lowercase
    info['first_name'] = "".join(random.sample(all_letters, 8))
    info['last_name'] = "".join(random.sample(all_letters, 8))

    print(info['email'], ' ', info['user_name'], ' ', info['first_name'], ' ', info['last_name'])
    return info

