import random

while True:
    n = int(input('Your n is: '))

    a= random.sample(range(0, 100000000), n)
    print(a)
