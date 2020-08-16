import os
import sys
import time
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# The setrecursionlimit function is 
# used to modify the default recursion 
# limit set by python(10^4). Using this,  
# we can increase the recursion limit 
# to satisfy our needs 
# Recursion limit is something, from what I understand,
# a limit that limits us so we don't create infinite calculations,
# but the current one can limit us from doing more than about 900 iterations.
# See more at https://www.geeksforgeeks.org/python-handling-recursion-limit/

sys.setrecursionlimit(10**6) 


def get_uptime(started_time):
    uptime = int(time.time() - started_time)
    seconds = int(uptime % 60)
    hours = int(uptime / 3600)
    minutes = int(uptime / 60 - (hours * 60))
    return "{0}h:{1}m:{2}s".format(hours, minutes, seconds)


password_to_hash = input("Password:").encode()
salt_file_name = input("Salt file name\n\t(new gets created if doesn't exist):")
times_to_derivate = int(input("Times to derivate the password:"))
ask_for_lenth = int(input("What length do you want your password to be?"))


def hash_the_password(password, salt, times_left, length_needed):
    if not times_left:
        return password.decode()
    password =str(password).encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=length_needed,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    hashed_password = base64.urlsafe_b64encode(kdf.derive(password))
    times_left -= 1
    print("Progress:", round((times_to_derivate-times_left)/times_to_derivate*100, 2), "%", "-",  hashed_password.decode())
    pw = hash_the_password(password=hashed_password, salt=salt, times_left=times_left, length_needed=length_needed)
    return pw
time_started = time.time()

if os.path.isfile(salt_file_name):
    # read from it
    with open(salt_file_name, 'rb') as temp_file:
        salt = temp_file.read()
else:
    # create and write to it
    salt = os.urandom(64)
    with open(salt_file_name, 'wb') as temp_file:
        temp_file.write(salt)

a = hash_the_password(password=password_to_hash, salt=salt, times_left=times_to_derivate, length_needed=ask_for_lenth)
# For some reason the hash isn't the exact length that the user gave..
print("Your new password is:", a[:ask_for_lenth])
print("Finished in:", get_uptime(time_started))
