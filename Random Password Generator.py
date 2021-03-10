import string
import random
import time

Ammount = input('How many passwords do you want?:')
Ammount = int(Ammount)

print("\n")

pswd_len = input("How long do you want the passwords?:")
pswd_len = int(pswd_len)

print("\n")

for x in range(Ammount):
    characters = string.ascii_letters + string.punctuation + string.digits
    
    password = "".join(random.choice(characters) for x in range(pswd_len))
    
    time.sleep(0.5)
    print(password)

time.sleep(0.5)
print("\nPlease Subscribe for more videos")