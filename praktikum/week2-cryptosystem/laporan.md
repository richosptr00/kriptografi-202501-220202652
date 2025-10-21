# Laporan Praktikum Kriptografi
Minggu ke-: **2** Topik: **Implementasi Caesar Cipher** Nama: **Richo Ali Hasan Saputra** NIM: **220202652** Kelas: **5IKKA** ---

## 1. Tujuan
Tujuan dari praktikum ini adalah **memahami konsep dasar *cipher* substitusi sederhana**, yaitu Caesar Cipher, dan **mengimplementasikannya menggunakan bahasa pemrograman Python** untuk proses enkripsi dan dekripsi. Mahasiswa diharapkan mampu menerapkan **operasi modular aritmetika** dalam konteks kriptografi.

---

## 2. Dasar Teori
Kriptografi klasik merupakan studi tentang teknik enkripsi dan dekripsi yang digunakan sebelum era komputer modern. Salah satu metode yang paling sederhana dan tertua adalah **Caesar Cipher** (atau *Shift Cipher*). Caesar Cipher adalah **cipher substitusi** di mana setiap huruf dalam *plaintext* diganti dengan huruf lain yang terletak sejumlah tetap posisi di bawahnya dalam alfabet.

Kunci rahasia (**$k$**) dalam Caesar Cipher adalah jumlah pergeseran. Proses enkripsi dan dekripsi didasarkan pada **modular aritmetika** ($\text{mod } N$), di mana $N$ adalah jumlah karakter dalam alfabet yang digunakan (biasanya $N=26$ untuk alfabet Latin). Secara matematis, proses enkripsi ($\text{E}$) dan dekripsi ($\text{D}$) untuk karakter $x$ dengan kunci $k$ adalah:
$$\text{Enkripsi: } E(x) = (x + k) \pmod{26}$$
$$\text{Dekripsi: } D(y) = (y - k) \pmod{26}$$
Meskipun Caesar Cipher mudah diimplementasikan, ia dianggap **tidak aman** di era modern karena memiliki ruang kunci (*keyspace*) yang sangat kecil (hanya 25 kemungkinan kunci non-trivial), yang membuatnya rentan terhadap serangan *brute-force* atau analisis frekuensi.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (Tidak diperlukan)

---

## 4. Langkah Percobaan
1. **Inisialisasi Proyek:** Membuat *repository* Git baru dan struktur folder `praktikum/week2-cryptosystem/src/`.
2. **Pembuatan File:** Membuat file `caesar_cipher.py` di dalam folder `praktikum/week2-cryptosystem/src/`.
3. **Implementasi Fungsi:** Menuliskan kode Python yang terdiri dari fungsi `encrypt(text, key)` dan `decrypt(text, key)` berdasarkan rumus modular aritmetika.
4. **Validasi Input:** Menambahkan logika untuk menangani huruf besar/kecil dan karakter non-alfabet (seperti spasi dan tanda baca).
5. **Uji Coba:** Menjalankan program dari *terminal* dengan perintah `python caesar_cipher.py` untuk menguji enkripsi dan dekripsi dengan *plaintext* dan kunci tertentu.
6. **Dokumentasi:** Menyusun laporan praktikum ini dan mencatat *commit log* pada Git.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi. Pastikan *indentation* sesuai.)

```python
# File: caesar_cipher.py

def encrypt(plaintext, key):
    """
    Mengenkripsi plaintext menggunakan Caesar Cipher (Shift Cipher).
    """
    result = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':
            # Enkripsi untuk huruf kapital
            char_index = ord(char) - ord('A')
            cipher_index = (char_index + key) % 26
            result += chr(cipher_index + ord('A'))
            
        elif 'a' <= char <= 'z':
            # Enkripsi untuk huruf kecil
            char_index = ord(char) - ord('a')
            cipher_index = (char_index + key) % 26
            result += chr(cipher_index + ord('a'))
            
        else:
            # Karakter non-alfabet tetap
            result += char
            
    return result

def decrypt(ciphertext, key):
    """
    Mendekripsi ciphertext yang dienkripsi menggunakan Caesar Cipher.
    """
    result = ""
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            # Dekripsi untuk huruf kapital
            char_index = ord(char) - ord('A')
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

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    text = "RICH ALI HASAN SAPUTRA, 220202652"
    shift = 3
    
    ciphertext = encrypt(text, shift)
    plaintext_decrypted = decrypt(ciphertext, shift)
    
    print(f"Plaintext Asli: {text}")
    print(f"Kunci Geser (k): {shift}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext Hasil Dekripsi: {plaintext_decrypted}")
