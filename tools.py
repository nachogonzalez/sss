import os
from cryptography.fernet import Fernet

def encrypt_files_in_folder(folder_path, key):
    """
    Encrypts all files in the specified folder using the provided key.

    :param folder_path: Path to the folder containing files to encrypt.
    :param key: Encryption key (must be a valid Fernet key).
    """
    fernet = Fernet(key)
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)

# Example usage:
# Generate a key (only do this once and save it securely)
# key = Fernet.generate_key()
# print(f"Encryption Key: {key.decode()}")

# Use the saved key to encrypt files
# encrypt_files_in_folder('path/to/folder', key)

def decrypt_files_in_folder(folder_path, key):
    """
    Decrypts all files in the specified folder using the provided key.

    :param folder_path: Path to the folder containing files to decrypt.
    :param key: Decryption key (must be a valid Fernet key).
    """
    fernet = Fernet(key)
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)

def get_system_type():
    """
    Returns a string indicating the type of operating system.

    :return: 'Windows' if the system is Windows, 'Linux' if the system is Linux.
    """
    if os.name == 'nt':
        return 'Windows'
    elif os.name == 'posix':
        return 'Linux'
    else:
        return 'Unknown'