from cryptography.fernet import Fernet
import os

# Functie om een sleutel te genereren en op te slaan in een bestand
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Functie om de sleutel te laden
def load_key():
    if os.path.exists("secret.key"):
        return open("secret.key", "rb").read()
    else:
        return generate_key()

# Functie om een bericht te versleutelen
def encrypt_message(message):
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Functie om een bericht te ontsleutelen
def decrypt_message(encrypted_message):
    key = load_key()
    f = Fernet(key)
    try:
        decrypted_message = f.decrypt(encrypted_message).decode()
        return decrypted_message
    except Exception as e:
        return f"Ontsleuteling mislukt: {e}"

# Command-line interface
def main():
    print("Welkom bij de Encryptie/Decryptie App")
    while True:
        keuze = input("\nWat wil je doen? (1: Versleutelen, 2: Ontsleutelen, 3: Afsluiten): ")
        if keuze == '1':
            message = input("Voer de tekst in die je wilt versleutelen: ")
            encrypted_message = encrypt_message(message)
            print(f"Versleutelde tekst: {encrypted_message.decode()}")
        elif keuze == '2':
            encrypted_message = input("Voer de versleutelde tekst in die je wilt ontsleutelen: ")
            decrypted_message = decrypt_message(encrypted_message.encode())
            print(f"Ontsleutelde tekst: {decrypted_message}")
        elif keuze == '3':
            print("Programma beëindigen...")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
