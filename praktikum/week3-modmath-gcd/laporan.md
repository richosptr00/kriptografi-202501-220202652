# Laporan Praktikum Kriptografi

Minggu ke-: 2
Topik: Implementasi Caesar Cipher Klasik
Nama: Richo Ali Hasan Saputra
NIM: 220202652
Kelas: 5IKKA

---

## 1. Tujuan

Tujuan dari praktikum ini adalah untuk:

1. Memahami prinsip dasar dari *substitution cipher* melalui algoritma Caesar Cipher.

2. Mampu mengimplementasikan algoritma enkripsi dan dekripsi Caesar Cipher menggunakan bahasa pemrograman Python.

3. Memahami peran aritmetika modular dalam operasi kriptografi klasik.

---

## 2. Dasar Teori

Caesar Cipher, atau terkadang disebut *shift cipher*, adalah salah satu bentuk kriptografi substitusi monoalfabetik tertua yang ditemukan oleh Julius Caesar. Algoritma ini bekerja dengan mengganti setiap huruf dalam *plaintext* dengan huruf lain yang terletak pada sejumlah posisi tetap (*key* atau kunci pergeseran) ke bawah di abjad.

Secara matematis, proses enkripsi $E$ untuk sebuah huruf $P$ dengan kunci $K$ didefinisikan sebagai:

$$
E(P) = (P + K) \mod 26
$$

Sedangkan proses dekripsi $D$ didefinisikan sebagai:

$$
D(C) = (C - K) \mod 26
$$

di mana $P$, $C$, dan $K$ adalah nilai numerik dari *plaintext* (huruf asli), *ciphertext* (huruf terenkripsi), dan kunci, dan operasi dilakukan dalam modulus 26 karena terdapat 26 huruf dalam abjad Latin. Prinsip aritmetika modular ini sangat penting untuk memastikan pergeseran huruf kembali ke awal abjad (A) setelah mencapai akhir abjad (Z), menjadikannya operasi yang siklik.

---

## 3. Alat dan Bahan

- Python 3.x

- Visual Studio Code / editor lain

- Git dan akun GitHub

- Tidak ada *library* tambahan yang diperlukan karena implementasi menggunakan fungsi dasar Python.

---

## 4. Langkah Percobaan

Berikut adalah langkah-langkah yang dilakukan dalam praktikum implementasi Caesar Cipher:

1. Membuat direktori kerja untuk praktikum minggu ini, misalnya `praktikum/week2-caesar/`.

2. Di dalam folder tersebut, membuat file Python baru bernama `caesar_cipher.py`.

3. Menyalin dan memodifikasi kode program implementasi Caesar Cipher yang mencakup fungsi enkripsi dan dekripsi.

4. Menjalankan program dengan perintah pada terminal: `python caesar_cipher.py`

5. Menguji program dengan berbagai *plaintext* dan nilai kunci, dan membandingkan hasilnya dengan perhitungan manual.

6. Melakukan *commit* dan *push* kode program dan laporan ke repositori GitHub.

---

## 5. Source Code

Berikut adalah kode program Python yang digunakan untuk mengimplementasikan Caesar Cipher:

```python:Caesar Cipher Implementation:caesar_cipher.py
# Implementasi Caesar Cipher Klasik

def encrypt(text, key):
    """
    Melakukan enkripsi Caesar Cipher pada teks.
    Hanya memproses huruf alfabet, mengabaikan spasi dan karakter lain.
    """
    result = ""
    # Memastikan kunci dalam rentang 0-25
    key = key % 26
    
    for char in text:
        if 'A' <= char <= 'Z':
            # Untuk huruf kapital
            # Ord('A') = 65. Menghitung posisi (0-25), menambahkan kunci, lalu modulo 26.
            # Kemudian menambahkan kembali Ord('A') untuk mendapatkan kode ASCII baru.
            encrypted_char_code = (ord(char) - ord('A') + key) % 26 + ord('A')
            result += chr(encrypted_char_code)
        elif 'a' <= char <= 'z':
            # Untuk huruf kecil
            encrypted
