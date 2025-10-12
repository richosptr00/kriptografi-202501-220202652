# Laporan Praktikum Kriptografi  
Minggu ke-: 11  
Topik: Secret Sharing  
Nama: Richo Ali Hasan Saputra  
NIM: 220202652  
Kelas: 1KEAS / 5IKKA  

---

## 1. Tujuan  
Memahami prinsip dasar dan implementasi algoritma Secret Sharing, khususnya skema Shamir's Secret Sharing, untuk membagi dan merekonstruksi informasi rahasia secara aman dan terdistribusi.

---

## 2. Dasar Teori  
Secret Sharing adalah metode kriptografi yang memungkinkan suatu rahasia dibagi menjadi beberapa bagian (share), sehingga hanya kombinasi tertentu dari bagian-bagian tersebut yang dapat digunakan untuk merekonstruksi rahasia. Teknik ini sangat berguna dalam sistem yang membutuhkan kolaborasi antar pihak untuk mengakses data sensitif.

Shamir's Secret Sharing adalah salah satu algoritma paling populer dalam kategori ini. Ia menggunakan polinomial acak dengan derajat _t-1_ (di mana _t_ adalah threshold) dan prinsip interpolasi Lagrange untuk merekonstruksi rahasia. Setiap share adalah hasil substitusi nilai _x_ ke dalam polinomial. Rahasia dapat direkonstruksi hanya jika jumlah share yang dikumpulkan ≥ _t_.

---

## 3. Alat dan Bahan  
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan: `sympy`, `random`

---

## 4. Langkah Percobaan  
1. Membuat file `secret_sharing.py` di folder `praktikum/week11-secret-sharing/src/`.  
2. Menyalin kode program dari modul praktikum.  
3. Menjalankan program dengan perintah `python secret_sharing.py`.  
4. Menguji pembagian dan rekonstruksi rahasia dengan berbagai kombinasi threshold dan jumlah share.

---

## 5. Source Code  
```python
from sympy import symbols, interpolate
import random

def generate_shares(secret, threshold, num_shares):
    x = symbols('x')
    coeffs = [secret] + [random.randint(1, 100) for _ in range(threshold - 1)]
    poly = sum(c * x**i for i, c in enumerate(coeffs))
    shares = [(i, poly.subs(x, i)) for i in range(1, num_shares + 1)]
    return shares

def reconstruct_secret(shares):
    x = symbols('x')
    points = [(s[0], s[1]) for s in shares]
    poly = interpolate(points, x)
    return poly.subs(x, 0)
