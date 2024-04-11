import re

def is_valid_password(password):
    regex = r'^(?=.[a-z])(?=(?:.[A-Z]){3,})(?!(?: Jan|Vlk)).{6,18}$'
    return bool(re.match(regex, password))

# Test cases
valid_passwords = ['Heslo123A', 'JanaNovakova12', 'Vltava456Bcd', 'TajneHeslo1234']
invalid_passwords = ['Jan', 'Vlk', 'heslo123', 'JanaNovakova', 'Vltava456']

print("Testing valid passwords:")
for password in valid_passwords:
    print(f"{password}: {is_valid_password(password)}")

print("\nTesting invalid passwords:")
for password in invalid_passwords:
    print(f"{password}: {is_valid_password(password)}")
