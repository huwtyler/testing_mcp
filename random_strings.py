# Write a script that outputs a list of random 5 alphanumeric strings.
# Containing uppercase letters and numbers only. The script should output 20 at a time.

import random
import string


def generate_random_strings(count=20, length=5):
    # 🤖 Build charset from uppercase letters and digits only
    charset = string.ascii_uppercase + string.digits
    return [''.join(random.choices(charset, k=length)) for _ in range(count)]


if __name__ == '__main__':
    # 🤖 Generate and print 20 random 5-character strings
    results = generate_random_strings()
    for s in results:
        print(s)
