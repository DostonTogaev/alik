import bcrypt

def hash_password(raw_password):
    encoded_password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded_password, salt)


new_password = input('?: ').encode('utf-8')

result = bcrypt.checkpw(new_password, hash_password('123'))
print(result)