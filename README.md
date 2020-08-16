# Password-Derivation
A password derivation tool. Helps keep your passwords large and secure, while making them easy to remember.

# How it works
Basically you can input a password as little as a 1 character in length. Then, the tool will create a salt file (do not lose!), with which it will derivate the password as many times as you told it. Finally, you will get the exact length of your password back.

# What you need to have and remember
You need to always have your salt file. If you loose the salt file you have created your password with - you.are.screwed. Back up your salt file.
So all you need to remember are 4 things:
- Where is your salt file
- What is your little password
- How many times have you derivated it
and
- What is the final length of your password.

An example would be:

password: a

salt file: salt1

times derivated: 100

final length: 128

# How to run it?
Inside the downloaded repository, run: **python3.8 password-derivation.py**

# What are it's use cases?
Well, password derivation makes brute-forcing someone's password very, very hard, if I dare even to say impossible. So in short - it turns a short-password-to-remember into a strong password that no one can guess. I use it; You should use it.

# Finally
Yes, advices on the code are still appreciated.
