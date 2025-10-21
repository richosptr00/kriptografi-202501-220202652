```python
# File: caesar_cipher.py

def encrypt(plaintext, key):
    """
    Mengenkripsi plaintext menggunakan Caesar Cipher (Shift Cipher).
    Setiap karakter alfabet digeser sejauh 'key' posisi.
    Karakter non-alfabet dibiarkan tidak berubah.
    """
    result = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':
            # Enkripsi untuk huruf kapital
            # 1. Ubah huruf ke indeks 0-25
            char_index = ord(char) - ord('A')
            # 2. Lakukan pergeseran dan modular aritmetika
            cipher_index = (char_index + key) % 26
            # 3. Ubah kembali indeks ke karakter
            result += chr(cipher_index + ord('A'))
            
        elif 'a' <= char <= 'z':
            # Enkripsi untuk huruf kecil
            char_index = ord(char) - ord('a')
            cipher_index = (char_index + key) % 26
            result += chr(cipher_index + ord('a'))
            
        else:
            # Karakter non-alfabet (spasi, angka, tanda baca) tetap
            result += char
            
    return result

def decrypt(ciphertext, key):
    """
    Mendekripsi ciphertext yang dienkripsi menggunakan Caesar Cipher.
    Operasi dekripsi adalah kebalikan dari enkripsi, yaitu (indeks - key) mod 26.
    """
    result = ""
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            # Dekripsi untuk huruf kapital
            char_index = ord(char) - ord('A')
            # Operasi Dekripsi: (index - key) MOD 26
            plain_index = (char_index - key) % 26
            result += chr(plain_index + ord('A'))
            
        elif 'a' <= char <= 'z':
            # Dekripsi untuk huruf kecil
            char_index = ord(char) - ord('a')
            plain_index = (char_index - key) % 26
            result += chr(plain_index + ord('a'))
            
        else:
            # Karakter non-alfabet tetap
            result += char
            
    return result

# --- Contoh Penggunaan (Opsional, bisa dihapus jika hanya ingin menampilkan fungsi utama) ---
if __name__ == "__main__":
    text = "RICH ALI HASAN SAPUTRA, 220202652"
    shift = 3
    
    ciphertext = encrypt(text, shift)
    plaintext_decrypted = decrypt(ciphertext, shift)
    
    print(f"Plaintext Asli: {text}")
    print(f"Kunci Geser (k): {shift}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext Hasil Dekripsi: {plaintext_decrypted}")
