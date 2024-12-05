from cryptography.fernet import Fernet

def encrypt_api_key(key):
    fernet = Fernet.generate_key()
    cipher_suite = Fernet(fernet)
    encrypted_key = cipher_suite.encrypt(key.encode())
    return encrypted_key

def decrypt_api_key(encrypted_key):
    fernet = Fernet.generate_key()
    cipher_suite = Fernet(fernet)
    decrypted_key = cipher_suite.decrypt(encrypted_key).decode()
    return decrypted_key
