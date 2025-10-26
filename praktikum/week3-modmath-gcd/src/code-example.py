# Implementasi Caesar Cipher Klasik

def encrypt(text, key):
    """
    Melakukan enkripsi Caesar Cipher pada teks.
    Hanya memproses huruf alfabet, mengabaikan angka (NIM) dan karakter lain.
    """
    result = ""
    # Memastikan kunci dalam rentang 0-25
    key = key % 26
    
    for char in text:
        if 'A' <= char <= 'Z':
            # Untuk huruf kapital
            # Hitung posisi (0-25), geser dengan kunci, modulo 26, lalu konversi kembali ke ASCII.
            encrypted_char_code = (ord(char) - ord('A') + key) % 26 + ord('A')
            result += chr(encrypted_char_code)
        elif 'a' <= char <= 'z':
            # Untuk huruf kecil
            encrypted_char_code = (ord(char) - ord('a') + key) % 26 + ord('a')
            result += chr(encrypted_char_code)
        else:
            # Mengabaikan karakter non-alfabet seperti angka (NIM), spasi, dan simbol
            result += char
            
    return result

def decrypt(text, key):
    """
    Melakukan dekripsi Caesar Cipher. Sama dengan enkripsi dengan kunci negatif.
    """
    # Dekripsi adalah Enkripsi dengan kunci yang membalikkan pergeseran (26 - key atau -key)
    return encrypt(text, -key)

# Main program untuk pengujian
if __name__ == "__main__":
    
    # Data Uji menggunakan NIM: 220202652
    plaintext = "DATA SAYA DENGAN NIM 220202652"
    key = 3 # Kunci pergeseran
    
    print("--- Caesar Cipher Klasik (Uji NIM) ---")
    print(f"Plaintext Asli: {plaintext}")
    print(f"Kunci (Shift): {key}")

    # Enkripsi
    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext (Terenkripsi): {ciphertext}")
    
    # Dekripsi
    decrypted_text = decrypt(ciphertext, key)
    print(f"Plaintext (Terdekripsi): {decrypted_text}")
    
    # Uji Kasus dengan kunci besar (misalnya 29)
    key_large = 29 # Setara dengan shift 3 (29 mod 26 = 3)
    ciphertext_large = encrypt(plaintext, key_large)
    decrypted_large = decrypt(ciphertext_large, key_large)
    print("\n--- Uji Kunci Besar ---")
    print(f"Plaintext Asli: {plaintext}")
    print(f"Kunci Besar: {key_large} (efektif shift {key_large % 26})")
    print(f"Ciphertext: {ciphertext_large}")
    print(f"Decrypted: {decrypted_large}")
