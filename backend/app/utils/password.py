import bcrypt

#   bcrypt.hashpw(password, salt)
def hash_password(password: str) -> str:
    password = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password, salt)
    return hashed_password.decode("utf-8")

#   bcrypt.checkpw(password, hashed_password)
def verify_password(password: str, hashed_password: str) -> bool:
    password_byte = password.encode("utf-8")
    hash_password_byte = hashed_password.encode("utf-8")
    return bcrypt.checkpw(password_byte, hash_password_byte)


