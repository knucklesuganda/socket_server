import settings


class Encryptor:
    def encrypt(self, text):
        encrypted_text = ""

        for symb in text:
            encrypted_text += chr(ord(symb) + settings.ENCRYPTION_KEY)

        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""

        for symb in text:
            decrypted_text += chr(ord(symb) - settings.ENCRYPTION_KEY)

        return decrypted_text

