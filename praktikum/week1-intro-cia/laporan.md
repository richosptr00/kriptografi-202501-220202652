# Laporan Praktikum Kriptografi  
Minggu ke-: 2  
Topik: Caesar Cipher  
Nama: Richo Ali Hasan Sputra  
NIM: 220202652  
Kelas: 5IKKA  

---

## 1. Tujuan  
Memahami cara kerja cipher klasik Caesar Cipher dan mengimplementasikan algoritma enkripsi dan dekripsi sederhana menggunakan Python.

---

## 2. Dasar Teori  
Caesar Cipher adalah salah satu bentuk cipher klasik yang bekerja dengan cara menggeser setiap huruf dalam teks asli sejumlah posisi tertentu dalam alfabet. Misalnya, dengan kunci 3, huruf A akan menjadi D, B menjadi E, dan seterusnya.

Cipher ini termasuk dalam kategori substitusi monoalfabetik, di mana setiap huruf digantikan oleh satu huruf lain berdasarkan aturan tetap. Meskipun sederhana dan mudah dipecahkan, Caesar Cipher merupakan dasar penting dalam memahami kriptografi klasik dan konsep enkripsi.

Modular aritmetika digunakan dalam Caesar Cipher untuk memastikan bahwa pergeseran huruf tetap berada dalam rentang alfabet. Misalnya, jika pergeseran melebihi huruf Z, maka akan kembali ke awal alfabet menggunakan operasi modulo.

---

## 3. Alat dan Bahan  
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (tidak diperlukan untuk Caesar Cipher)

---

## 4. Langkah Percobaan  
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.  
2. Menyalin kode program dari panduan praktikum.  
3. Menjalankan program dengan perintah `python caesar_cipher.py`.

---

## 5. Source Code  
```python
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

# Contoh penggunaan
plain_text = "Kriptografi"
key = 3
cipher_text = encrypt(plain_text, key)
print("Encrypted:", cipher_text)
print("Decrypted:", decrypt(cipher_text, key))
