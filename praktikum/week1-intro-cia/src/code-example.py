# caesar_cipher_nim.py

def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

def main():
    nim = "220202652"
    key = sum(int(digit) for digit in nim)  # hasil: 21
    print("=== Caesar Cipher dengan NIM ===")
    print("Kunci (jumlah digit NIM):", key)

    text = input("Masukkan teks yang ingin dienkripsi: ")
    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("Teks terenkripsi:", encrypted)
    print("Teks terdekripsi:", decrypted)

if __name__ == "__main__":
    main()
