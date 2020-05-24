# Алгоритм
# Передача ключа


class Encryptor:
    def __init__(self):
        self.key = 20

    def encrypt(self, text):
        encrypted_text = ""

        for symb in text:
            encrypted_text += chr(ord(symb) + self.key)

        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""

        for symb in text:
            decrypted_text += chr(ord(symb) - self.key)

        return decrypted_text

