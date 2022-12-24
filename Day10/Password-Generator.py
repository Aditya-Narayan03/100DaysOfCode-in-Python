import secrets
import string

input = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

password = ''
password = ''.join(secrets.choice(input) for ch in range(16))
print("Your password is : ", password)