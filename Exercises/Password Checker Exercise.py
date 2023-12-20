username = input('Enter your username: ')
password = input('Enter your password: ')
password_length = len(password)
password_hidden = '*' * password_length

print(f"Hello {username}! The password {password_hidden} is {password_length} characters long")